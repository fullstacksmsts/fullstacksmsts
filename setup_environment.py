#!/usr/bin/env python3
"""
Setup Environment Script for fullstacksmsts.co.uk SEO Automation
This script sets up the necessary directories and dependencies for the SEO automation system.
"""

import os
import sys
import json
import logging
import subprocess
import argparse
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('Setup_Environment')

# Load environment variables
load_dotenv()

class SetupEnvironment:
    """Class to set up the SEO automation environment."""
    
    def __init__(self, config_file=None):
        """Initialize the setup environment."""
        self.config_file = config_file or "config.json"
        self.config = self._load_config()
        
        # Define required directories
        self.required_directories = [
            "data",
            "data/keywords",
            "data/ai_cache",
            "logs",
            "output",
            "output/content",
            "output/content/articles",
            "output/content/briefs",
            "output/content/keyword_analysis",
            "output/content/competitor_analysis",
            "output/content/locations",
            "reports",
            "templates",
            "templates/blog_posts",
            "templates/location_pages",
            "scripts",
            "scripts/keyword_analysis",
            "scripts/technical_seo",
            "scripts/content_generation",
            "scripts/reporting",
            "scripts/ai_assistant"
        ]
        
        # Define required packages
        self.required_packages = [
            "pandas",
            "numpy",
            "requests",
            "beautifulsoup4",
            "openpyxl",
            "python-dotenv",
            "markdown",
            "jinja2",
            "schedule",
            "tqdm",
            "colorama"
        ]
    
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
            "ai_assistant": {
                "default": "claude",
                "cache_ttl": 604800,
                "claude": {
                    "model": "claude-3-sonnet-20240229",
                    "max_tokens": 4000,
                    "temperature": 0.7
                },
                "deepseek": {
                    "model": "deepseek-r1-chat",
                    "max_tokens": 4000,
                    "temperature": 0.7
                },
                "gemini": {
                    "model": "gemini-pro",
                    "max_tokens": 4000,
                    "temperature": 0.7
                }
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
                "user_agent": "SEOAutomationBot/1.0",
                "check_items": [
                    "meta_tags",
                    "headings",
                    "images",
                    "links",
                    "structured_data",
                    "core_web_vitals",
                    "mobile_friendliness",
                    "page_speed",
                    "https",
                    "canonical_tags"
                ]
            },
            "content_generation": {
                "templates_dir": "templates",
                "output_dir": "output/content",
                "content_types": [
                    "pillar_content",
                    "location_pages",
                    "blog_posts",
                    "service_pages"
                ]
            },
            "reporting": {
                "report_type": "monthly",
                "metrics": [
                    "organic_traffic",
                    "keyword_rankings",
                    "conversion_rate",
                    "technical_issues",
                    "content_performance"
                ],
                "email_recipients": [
                    "seo@fullstacksmsts.co.uk",
                    "marketing@fullstacksmsts.co.uk"
                ]
            },
            "scheduling": {
                "keyword_research": "monthly",
                "technical_audit": "weekly",
                "content_generation": "weekly",
                "reporting": "monthly"
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
    
    def create_directories(self):
        """Create necessary directories."""
        for directory in self.required_directories:
            os.makedirs(directory, exist_ok=True)
        
        logger.info("Directory structure created successfully.")
    
    def install_dependencies(self):
        """Install required Python packages."""
        logger.info("Installing required Python packages...")
        
        try:
            # Check if pip is available
            subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
            
            # Install required packages
            for package in self.required_packages:
                logger.info(f"Installing {package}...")
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            
            logger.info("All required packages installed successfully.")
            return True
        
        except subprocess.CalledProcessError as e:
            logger.error(f"Error installing packages: {str(e)}")
            return False
    
    def create_env_file(self):
        """Create .env file with API keys."""
        logger.info("Creating .env file...")
        
        env_file = ".env"
        
        # Check if .env file already exists
        if os.path.exists(env_file):
            logger.info(f"{env_file} already exists. Skipping creation.")
            return True
        
        # Create .env file with placeholders
        try:
            with open(env_file, 'w') as f:
                f.write("# API Keys for SEO Automation\n\n")
                f.write("# Google API Keys\n")
                f.write("GOOGLE_API_KEY=your_google_api_key\n")
                f.write("GOOGLE_SEARCH_CONSOLE_CLIENT_ID=your_search_console_client_id\n")
                f.write("GOOGLE_SEARCH_CONSOLE_CLIENT_SECRET=your_search_console_client_secret\n")
                f.write("GOOGLE_ANALYTICS_CLIENT_ID=your_analytics_client_id\n")
                f.write("GOOGLE_ANALYTICS_CLIENT_SECRET=your_analytics_client_secret\n\n")
                
                f.write("# AI Assistant API Keys\n")
                f.write("CLAUDE_API_KEY=your_claude_api_key\n")
                f.write("DEEPSEEK_API_KEY=your_deepseek_api_key\n")
                f.write("GEMINI_API_KEY=your_gemini_api_key\n\n")
                
                f.write("# SEO Tool API Keys\n")
                f.write("SERPSTAT_API_KEY=your_serpstat_api_key\n")
                f.write("UBERSUGGEST_EMAIL=your_ubersuggest_email\n")
                f.write("UBERSUGGEST_PASSWORD=your_ubersuggest_password\n\n")
                
                f.write("# Email Configuration\n")
                f.write("EMAIL_SENDER=your_email_sender\n")
                f.write("EMAIL_PASSWORD=your_email_password\n")
                f.write("SMTP_SERVER=smtp.gmail.com\n")
                f.write("SMTP_PORT=587\n")
                f.write("NOTIFICATION_EMAIL=your_notification_email\n")
            
            logger.info(f"{env_file} created successfully.")
            logger.info(f"Please update {env_file} with your actual API keys and credentials.")
            return True
        
        except Exception as e:
            logger.error(f"Error creating {env_file}: {str(e)}")
            return False
    
    def create_template_files(self):
        """Create template files."""
        logger.info("Creating template files...")
        
        # Create pillar content template
        pillar_template_path = "templates/blog_posts/pillar_content_template.md"
        if not os.path.exists(pillar_template_path):
            try:
                with open(pillar_template_path, 'w') as f:
                    f.write("---\n")
                    f.write("title: ${title}\n")
                    f.write("meta_description: ${meta_description}\n")
                    f.write("keywords: ${keywords}\n")
                    f.write("pillar: ${pillar}\n")
                    f.write("date: ${date}\n")
                    f.write("---\n\n")
                    f.write("# ${title}\n\n")
                    f.write("## Introduction\n\n")
                    f.write("${introduction}\n\n")
                    f.write("## ${section1_title}\n\n")
                    f.write("${section1_content}\n\n")
                    f.write("## ${section2_title}\n\n")
                    f.write("${section2_content}\n\n")
                    f.write("## ${section3_title}\n\n")
                    f.write("${section3_content}\n\n")
                    f.write("## ${section4_title}\n\n")
                    f.write("${section4_content}\n\n")
                    f.write("## ${section5_title}\n\n")
                    f.write("${section5_content}\n\n")
                    f.write("## Conclusion\n\n")
                    f.write("${conclusion}\n\n")
                    f.write("---\n\n")
                    f.write("Book your SMSTS course today for just £360+VAT. With our 98% pass rate and flexible scheduling options, we make it easy to get certified. [Book Now](#)")
                
                logger.info(f"{pillar_template_path} created successfully.")
            
            except Exception as e:
                logger.error(f"Error creating {pillar_template_path}: {str(e)}")
        
        # Create location page template
        location_template_path = "templates/location_pages/location_page_template.md"
        if not os.path.exists(location_template_path):
            try:
                with open(location_template_path, 'w') as f:
                    f.write("---\n")
                    f.write("title: SMSTS Course in ${location}\n")
                    f.write("meta_description: Book your SMSTS course in ${location} for just £360+VAT. 98% pass rate, flexible scheduling options, and CITB accreditation.\n")
                    f.write("keywords: SMSTS course ${location}, ${location} SMSTS training, SMSTS course in ${location}\n")
                    f.write("location: ${location}\n")
                    f.write("date: ${date}\n")
                    f.write("---\n\n")
                    f.write("# SMSTS Course in ${location}\n\n")
                    f.write("## About SMSTS Courses in ${location}\n\n")
                    f.write("${about_content}\n\n")
                    f.write("## Why Choose Our SMSTS Courses in ${location}\n\n")
                    f.write("${why_choose_content}\n\n")
                    f.write("## SMSTS Course Details\n\n")
                    f.write("${course_details}\n\n")
                    f.write("## SMSTS Course Locations in ${location}\n\n")
                    f.write("${locations_content}\n\n")
                    f.write("## Book Your SMSTS Course in ${location}\n\n")
                    f.write("${booking_content}\n\n")
                    f.write("---\n\n")
                    f.write("Book your SMSTS course in ${location} today for just £360+VAT. With our 98% pass rate and flexible scheduling options, we make it easy to get certified. [Book Now](#)")
                
                logger.info(f"{location_template_path} created successfully.")
            
            except Exception as e:
                logger.error(f"Error creating {location_template_path}: {str(e)}")
        
        logger.info("Template files created successfully.")
    
    def setup(self):
        """Set up the SEO automation environment."""
        logger.info("Setting up SEO automation environment...")
        
        # Create directories
        self.create_directories()
        
        # Install dependencies
        self.install_dependencies()
        
        # Create .env file
        self.create_env_file()
        
        # Create template files
        self.create_template_files()
        
        logger.info("SEO automation environment setup completed successfully.")
        logger.info("Next steps:")
        logger.info("1. Update the .env file with your API keys and credentials")
        logger.info("2. Run the master automation script: python master_automation.py")
        logger.info("3. Check the logs directory for detailed logs")
        logger.info("4. Check the output directory for generated content")
        logger.info("5. Check the reports directory for generated reports")

def main():
    """Main function to set up the SEO automation environment."""
    parser = argparse.ArgumentParser(description="Setup Environment for SEO Automation")
    parser.add_argument("--config", help="Configuration file path")
    
    args = parser.parse_args()
    
    setup = SetupEnvironment(args.config)
    setup.setup()

if __name__ == "__main__":
    main()
