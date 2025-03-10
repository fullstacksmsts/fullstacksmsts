

#!/usr/bin/env python3
"""
Master Automation Script for fullstacksmsts.co.uk SEO
This script orchestrates the entire SEO automation process.
"""

import os
import sys
import logging
import argparse
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Import custom modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from scripts.keyword_analysis import keyword_research
    from scripts.technical_seo import technical_audit
    from scripts.content_generation import content_generator, location_page_generator
    from scripts.reporting import report_generator
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all required scripts are in the correct directories.")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/seo_automation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("Master_Automation")

# Load environment variables
load_dotenv()

class SEOAutomation:
    """Class to handle the SEO automation process."""
    
    def __init__(self, config_file=None):
        """Initialize the SEO automation system."""
        self.config_file = config_file or "config.json"
        self.config = self._load_config()
        
        # Create necessary directories
        self._create_directories()
    
    def _load_config(self):
        """Load configuration from JSON file."""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            logger.info(f"Configuration loaded from {self.config_file}")
            return config
        except FileNotFoundError:
            logger.warning(f"Configuration file {self.config_file} not found. Using default configuration.")
            return self._create_default_config()
        except json.JSONDecodeError:
            logger.error(f"Error parsing configuration file {self.config_file}. Using default configuration.")
            return self._create_default_config()
    
    def _create_default_config(self):
        """Create default configuration."""
        config = {
            "website": {
                "url": "https://fullstacksmsts.co.uk",
                "name": "Full Stack SMSTS",
                "content_pillars": [
                    "Understanding CITB SMSTS Courses",
                    "Navigating SMSTS Course Delivery and Providers",
                    "SMSTS Course Content and Assessment",
                    "SMSTS vs. Other Certifications",
                    "Implementing SMSTS Knowledge on Site"
                ]
            },
            "keyword_research": {
                "seed_keywords": [
                    "smsts course",
                    "smsts training",
                    "site management safety training scheme",
                    "citb smsts",
                    "smsts online"
                ],
                "competitors": [
                    "smsts-course.co.uk",
                    "knightlearning.co.uk",
                    "tamtraining.co.uk",
                    "goldcrosstraining.co.uk",
                    "3btraining.com"
                ],
                "locations": [
                    "London",
                    "Manchester",
                    "Birmingham",
                    "Glasgow",
                    "Leeds"
                ]
            },
            "technical_audit": {
                "crawl_depth": 3,
                "user_agent": "SEOAutomationBot/1.0"
            },
            "content_generation": {
                "templates_dir": "templates",
                "output_dir": "output/content"
            },
            "reporting": {
                "report_type": "monthly",
                "email_recipients": [
                    "seo@fullstacksmsts.co.uk",
                    "marketing@fullstacksmsts.co.uk"
                ]
            }
        }
        
        # Save default configuration
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            logger.info(f"Default configuration saved to {self.config_file}")
        except Exception as e:
            logger.error(f"Error saving default configuration: {str(e)}")
        
        return config
    
    def _create_directories(self):
        """Create necessary directories."""
        directories = [
            "data",
            "data/keywords",
            "logs",
            "output",
            "output/content",
            "output/content/locations",
            "reports",
            "templates",
            "templates/blog_posts",
            "templates/location_pages"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        
        logger.info("Directory structure created successfully.")
    
    def run_keyword_research(self):
        """Run keyword research process."""
        logger.info("Starting keyword research process...")
        
        try:
            # Get configuration
            seed_keywords = self.config["keyword_research"]["seed_keywords"]
            competitors = self.config["keyword_research"]["competitors"]
            locations = self.config["keyword_research"]["locations"]
            content_pillars = self.config["website"]["content_pillars"]
            
            # Create keyword combinations
            keyword_combinations = []
            for seed in seed_keywords:
                keyword_combinations.append(seed)
                for location in locations:
                    keyword_combinations.append(f"{seed} {location}")
                    keyword_combinations.append(f"{location} {seed}")
            
            # Add additional keyword variations
            variations = [
                "online", "weekend", "cost", "price", "refresher",
                "certification", "exam", "test", "course dates",
                "near me", "training", "providers"
            ]
            
            for seed in seed_keywords:
                for variation in variations:
                    keyword_combinations.append(f"{seed} {variation}")
            
            # Remove duplicates
            keyword_combinations = list(set(keyword_combinations))
            
            # Create a DataFrame to store keyword data
            keywords_df = pd.DataFrame({
                'keyword': keyword_combinations,
                'search_volume': [0] * len(keyword_combinations),  # Placeholder
                'difficulty': [0] * len(keyword_combinations),     # Placeholder
                'cpc': [0.0] * len(keyword_combinations),          # Placeholder
                'current_rank': [0] * len(keyword_combinations)    # Placeholder
            })
            
            # Assign content pillars to keywords
            pillar_assignments = {
                "Understanding CITB SMSTS Courses": [
                    "smsts course", "what is smsts", "citb smsts", 
                    "smsts meaning", "smsts certification", "smsts accreditation"
                ],
                "Navigating SMSTS Course Delivery and Providers": [
                    "smsts course providers", "smsts training", "smsts course online",
                    "weekend smsts course", "smsts course near me", "smsts course cost",
                    "smsts course price", "smsts course dates"
                ],
                "SMSTS Course Content and Assessment": [
                    "smsts exam", "smsts test", "smsts course content",
                    "smsts mock test", "smsts exam questions", "smsts pass rate",
                    "smsts certificate", "smsts course duration"
                ],
                "SMSTS vs. Other Certifications": [
                    "smsts vs sssts", "smsts vs nebosh", "smsts vs iosh",
                    "smsts equivalent", "smsts alternatives", "smsts or sssts",
                    "construction safety certifications"
                ],
                "Implementing SMSTS Knowledge on Site": [
                    "smsts site management", "applying smsts knowledge",
                    "smsts best practices", "smsts site safety", "smsts responsibilities",
                    "smsts risk assessment", "smsts method statements"
                ]
            }
            
            # Add pillar column to DataFrame
            keywords_df['pillar'] = ''
            
            # Assign pillars based on keyword matching
            for pillar, pillar_keywords in pillar_assignments.items():
                for pillar_keyword in pillar_keywords:
                    keywords_df.loc[keywords_df['keyword'].str.contains(pillar_keyword, case=False), 'pillar'] = pillar
            
            # Assign location keywords to the "Navigating SMSTS Course Delivery and Providers" pillar
            for location in locations:
                keywords_df.loc[keywords_df['keyword'].str.contains(location, case=False), 'pillar'] = "Navigating SMSTS Course Delivery and Providers"
            
            # Add journey stage column
            keywords_df['journey_stage'] = ''
            
            # Assign journey stages based on keyword intent
            awareness_keywords = ["what is", "meaning", "guide", "explained", "introduction", "basics"]
            consideration_keywords = ["compare", "vs", "versus", "difference", "review", "best", "top", "cost", "price"]
            conversion_keywords = ["book", "buy", "register", "sign up", "enroll", "course dates", "near me"]
            
            for keyword in awareness_keywords:
                keywords_df.loc[keywords_df['keyword'].str.contains(keyword, case=False), 'journey_stage'] = "awareness"
            
            for keyword in consideration_keywords:
                keywords_df.loc[keywords_df['keyword'].str.contains(keyword, case=False), 'journey_stage'] = "consideration"
            
            for keyword in conversion_keywords:
                keywords_df.loc[keywords_df['keyword'].str.contains(keyword, case=False), 'journey_stage'] = "conversion"
            
            # Default to "consideration" for any remaining keywords
            keywords_df.loc[keywords_df['journey_stage'] == '', 'journey_stage'] = "consideration"
            
            # Save keyword data
            output_file = "data/keywords/keyword_research_results.xlsx"
            keywords_df.to_excel(output_file, index=False)
            
            # Create location-specific keyword file
            location_keywords = keywords_df[keywords_df['keyword'].str.contains('|'.join(locations), case=False)]
            location_output_file = "data/keywords/location_keywords.csv"
            location_keywords.to_csv(location_output_file, index=False)
            
            logger.info(f"Keyword research completed successfully. Results saved to {output_file}")
            return True
        
        except Exception as e:
            logger.error(f"Error in keyword research process: {str(e)}")
            return False
    
    def run_technical_audit(self):
        """Run technical SEO audit process."""
        logger.info("Starting technical SEO audit process...")
        
        try:
            # Get configuration
            website_url = self.config["website"]["url"]
            crawl_depth = self.config["technical_audit"]["crawl_depth"]
            
            # Run technical audit
            output_file = f"reports/technical_audit_{datetime.now().strftime('%Y%m%d')}.xlsx"
            technical_audit.main(website_url, crawl_depth, output_file)
            
            logger.info(f"Technical SEO audit completed successfully. Results saved to {output_file}")
            return True
        
        except Exception as e:
            logger.error(f"Error in technical SEO audit process: {str(e)}")
            return False
    
    def run_content_generation(self):
        """Run content generation process."""
        logger.info("Starting content generation process...")
        
        try:
            # Get configuration
            templates_dir = self.config["content_generation"]["templates_dir"]
            output_dir = self.config["content_generation"]["output_dir"]
            content_pillars = self.config["website"]["content_pillars"]
            locations = self.config["keyword_research"]["locations"]
            
            # Check if AI assistant is configured
            use_ai = "ai_assistant" in self.config
            
            if use_ai:
                logger.info("Using AI-enhanced content generation")
                # Import AI-enhanced content generator
                from scripts.content_generation.ai_enhanced_content_generator import AIEnhancedContentGenerator
                
                # Initialize AI-enhanced content generator
                ai_generator = AIEnhancedContentGenerator()
                
                # Generate pillar content
                for i, pillar in enumerate(content_pillars):
                    logger.info(f"Generating AI-enhanced content for pillar: {pillar}")
                    ai_generator.generate_pillar_content(i)
                
                # Generate location content
                for location in locations:
                    logger.info(f"Generating AI-enhanced content for location: {location}")
                    ai_generator.generate_location_content(location)
            else:
                logger.info("Using template-based content generation")
                # Generate pillar content using templates
                pillar_template = f"{templates_dir}/blog_posts/pillar_content_template.md"
                keywords_file = "data/keywords/keyword_research_results.xlsx"
                
                # Create template file if it doesn't exist
                if not os.path.exists(pillar_template):
                    os.makedirs(os.path.dirname(pillar_template), exist_ok=True)
                    with open(pillar_template, 'w') as f:
                        f.write("# ${title}\n\n## ${subtitle}\n\n${content}")
                
                # Run content generator
                content_generator.main(pillar_template, keywords_file, output_dir)
                
                # Generate location pages
                location_template = f"{templates_dir}/location_pages/location_page_template.md"
                location_keywords_file = "data/keywords/location_keywords.csv"
                location_output_dir = f"{output_dir}/locations"
                
                # Create template file if it doesn't exist
                if not os.path.exists(location_template):
                    os.makedirs(os.path.dirname(location_template), exist_ok=True)
                    with open(location_template, 'w') as f:
                        f.write("# SMSTS Course in ${location}\n\n## About SMSTS Courses in ${location}\n\n${content}")
                
                # Generate content for each location
                for location in locations:
                    location_page_generator.main(location_template, location_keywords_file, location, location_output_dir)
            
            logger.info(f"Content generation completed successfully. Content saved to {output_dir}")
            return True
        
        except Exception as e:
            logger.error(f"Error in content generation process: {str(e)}")
            return False
    
    def run_reporting(self):
        """Run reporting process."""
        logger.info("Starting reporting process...")
        
        try:
            # Get configuration
            report_type = self.config["reporting"]["report_type"]
            
            # Set date range
            end_date = datetime.now().strftime('%Y-%m-%d')
            
            if report_type == "monthly":
                # Last 30 days
                start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            elif report_type == "quarterly":
                # Last 90 days
                start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
            else:  # annual
                # Last 365 days
                start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
            
            # Run report generator
            output_file = f"reports/{report_type}_seo_report_{datetime.now().strftime('%Y%m%d')}.xlsx"
            report_generator.main(start_date, end_date, report_type, output_file)
            
            logger.info(f"Reporting completed successfully. Report saved to {output_file}")
            return True
        
        except Exception as e:
            logger.error(f"Error in reporting process: {str(e)}")
            return False
    
    def run_all(self):
        """Run all SEO automation processes."""
        logger.info("Starting full SEO automation process...")
        
        # Run keyword research
        keyword_research_success = self.run_keyword_research()
        if not keyword_research_success:
            logger.warning("Keyword research process failed. Continuing with other processes...")
        
        # Run technical audit
        technical_audit_success = self.run_technical_audit()
        if not technical_audit_success:
            logger.warning("Technical audit process failed. Continuing with other processes...")
        
        # Run content generation
        content_generation_success = self.run_content_generation()
        if not content_generation_success:
            logger.warning("Content generation process failed. Continuing with other processes...")
        
        # Run reporting
        reporting_success = self.run_reporting()
        if not reporting_success:
            logger.warning("Reporting process failed.")
        
        # Check overall success
        overall_success = all([
            keyword_research_success,
            technical_audit_success,
            content_generation_success,
            reporting_success
        ])
        
        if overall_success:
            logger.info("Full SEO automation process completed successfully.")
        else:
            logger.warning("Full SEO automation process completed with some failures.")
        
        return overall_success

def main(process=None, config_file=None):
    """Main function to run SEO automation."""
    # Create SEO automation instance
    seo_automation = SEOAutomation(config_file)
    
    # Run specified process or all processes
    if process == "keyword_research":
        return seo_automation.run_keyword_research()
    elif process == "technical_audit":
        return seo_automation.run_technical_audit()
    elif process == "content_generation":
        return seo_automation.run_content_generation()
    elif process == "reporting":
        return seo_automation.run_reporting()
    else:
        return seo_automation.run_all()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEO Automation for fullstacksmsts.co.uk")
    parser.add_argument("--process", choices=["keyword_research", "technical_audit", "content_generation", "reporting", "all"], default="all", help="Process to run")
    parser.add_argument("--config", help="Configuration file path")
    
    args = parser.parse_args()
    main(args.process, args.config)
