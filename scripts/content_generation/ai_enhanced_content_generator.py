#!/usr/bin/env python3
"""
AI-Enhanced Content Generator for fullstacksmsts.co.uk
This script uses AI assistants to enhance the content generation process.
"""

import os
import sys
import json
import logging
import pandas as pd
from datetime import datetime

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ai_assistant.ai_assistant_manager import AIAssistantManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/ai_content_generator.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('AI_Enhanced_Content_Generator')

class AIEnhancedContentGenerator:
    """Generate SEO-optimized content using AI assistants."""
    
    def __init__(self, config_file=None):
        """Initialize the AI-enhanced content generator."""
        self.config_file = config_file or "config.json"
        self.config = self._load_config()
        
        # Initialize AI Assistant Manager
        self.ai_manager = AIAssistantManager(self.config_file)
        
        # Set up directories
        self.templates_dir = self.config.get("content_generation", {}).get("templates_dir", "templates")
        self.output_dir = self.config.get("content_generation", {}).get("output_dir", "output/content")
        
        # Ensure directories exist
        os.makedirs(self.templates_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load content pillars
        self.content_pillars = self.config.get("website", {}).get("content_pillars", [])
        
        logger.info("AI-Enhanced Content Generator initialized")
    
    def _load_config(self):
        """Load configuration from JSON file."""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            return config
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            return {}
    
    def _load_keywords(self, keywords_file=None):
        """Load keywords from file."""
        if not keywords_file:
            keywords_file = "data/keywords/keyword_research_results.xlsx"
        
        try:
            if os.path.exists(keywords_file):
                keywords_df = pd.read_excel(keywords_file)
                return keywords_df
            else:
                logger.warning(f"Keywords file not found: {keywords_file}")
                return pd.DataFrame()
        except Exception as e:
            logger.error(f"Error loading keywords: {str(e)}")
            return pd.DataFrame()
    
    def generate_content_brief(self, topic, pillar, keywords=None):
        """Generate a content brief for a topic."""
        logger.info(f"Generating content brief for topic: {topic}")
        
        # If keywords not provided, load from file
        if not keywords:
            keywords_df = self._load_keywords()
            if not keywords_df.empty:
                # Filter keywords by pillar
                pillar_keywords = keywords_df[keywords_df['pillar'] == pillar]
                if not pillar_keywords.empty:
                    keywords = pillar_keywords['keyword'].tolist()[:10]  # Use top 10 keywords
                else:
                    keywords = []
        
        # If still no keywords, use default ones
        if not keywords:
            keywords = [
                f"{topic}",
                "SMSTS course",
                "CITB SMSTS",
                "site management safety training"
            ]
        
        # Generate content brief using AI assistant
        content_brief = self.ai_manager.create_content_brief(topic, keywords, pillar)
        
        # Save content brief to file
        brief_dir = os.path.join(self.output_dir, "briefs")
        os.makedirs(brief_dir, exist_ok=True)
        
        filename = f"{topic.lower().replace(' ', '_')}_brief.md"
        brief_path = os.path.join(brief_dir, filename)
        
        with open(brief_path, 'w', encoding='utf-8') as f:
            f.write(f"# Content Brief: {topic}\n\n")
            f.write(f"Content Pillar: {pillar}\n\n")
            f.write(f"Target Keywords: {', '.join(keywords)}\n\n")
            f.write("---\n\n")
            f.write(content_brief)
        
        logger.info(f"Content brief saved to {brief_path}")
        
        return {
            "topic": topic,
            "pillar": pillar,
            "keywords": keywords,
            "brief": content_brief,
            "brief_path": brief_path
        }
    
    def generate_content(self, topic, pillar, keywords=None, brief=None):
        """Generate content for a topic."""
        logger.info(f"Generating content for topic: {topic}")
        
        # If brief not provided, generate one
        if not brief:
            brief_result = self.generate_content_brief(topic, pillar, keywords)
            brief = brief_result["brief"]
            keywords = brief_result["keywords"]
        
        # Extract key elements from the brief to use as a starting point
        # This is a simplified approach - in a real implementation, you would parse the brief more thoroughly
        content_sections = []
        current_section = ""
        
        for line in brief.split('\n'):
            if line.startswith('# ') or line.startswith('## ') or line.startswith('### '):
                if current_section:
                    content_sections.append(current_section)
                current_section = line + "\n\n"
            else:
                current_section += line + "\n"
        
        if current_section:
            content_sections.append(current_section)
        
        # Generate initial content based on the brief sections
        initial_content = "\n".join(content_sections)
        
        # Optimize content using AI assistant
        optimized_content = self.ai_manager.optimize_content(initial_content, keywords, pillar)
        
        # Generate meta description
        meta_description = self.ai_manager.generate_meta_description(optimized_content, keywords[0] if keywords else topic)
        
        # Save content to file
        content_dir = os.path.join(self.output_dir, "articles")
        os.makedirs(content_dir, exist_ok=True)
        
        filename = f"{topic.lower().replace(' ', '_')}.md"
        content_path = os.path.join(content_dir, filename)
        
        with open(content_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            f.write(f"title: {topic}\n")
            f.write(f"meta_description: {meta_description}\n")
            f.write(f"keywords: {', '.join(keywords) if keywords else topic}\n")
            f.write(f"pillar: {pillar}\n")
            f.write(f"date: {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"---\n\n")
            f.write(optimized_content)
        
        logger.info(f"Content saved to {content_path}")
        
        return {
            "topic": topic,
            "pillar": pillar,
            "keywords": keywords,
            "content": optimized_content,
            "meta_description": meta_description,
            "content_path": content_path
        }
    
    def analyze_keywords(self, keywords):
        """Analyze keywords using AI assistant."""
        logger.info(f"Analyzing {len(keywords)} keywords")
        
        # Analyze keywords using AI assistant
        keyword_analysis = self.ai_manager.analyze_keywords(keywords)
        
        # Save analysis to file
        analysis_dir = os.path.join(self.output_dir, "keyword_analysis")
        os.makedirs(analysis_dir, exist_ok=True)
        
        filename = f"keyword_analysis_{datetime.now().strftime('%Y%m%d')}.md"
        analysis_path = os.path.join(analysis_dir, filename)
        
        with open(analysis_path, 'w', encoding='utf-8') as f:
            f.write(f"# Keyword Analysis\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"Keywords: {', '.join(keywords)}\n\n")
            f.write("---\n\n")
            f.write(keyword_analysis)
        
        logger.info(f"Keyword analysis saved to {analysis_path}")
        
        return {
            "keywords": keywords,
            "analysis": keyword_analysis,
            "analysis_path": analysis_path
        }
    
    def analyze_competitor_content(self, competitor_url, competitor_content):
        """Analyze competitor content using AI assistant."""
        logger.info(f"Analyzing competitor content: {competitor_url}")
        
        # Analyze competitor content using AI assistant
        competitor_analysis = self.ai_manager.analyze_competitor(competitor_url, competitor_content)
        
        # Save analysis to file
        analysis_dir = os.path.join(self.output_dir, "competitor_analysis")
        os.makedirs(analysis_dir, exist_ok=True)
        
        # Extract domain from URL for filename
        domain = competitor_url.replace('https://', '').replace('http://', '').split('/')[0]
        filename = f"{domain}_analysis_{datetime.now().strftime('%Y%m%d')}.md"
        analysis_path = os.path.join(analysis_dir, filename)
        
        with open(analysis_path, 'w', encoding='utf-8') as f:
            f.write(f"# Competitor Content Analysis: {competitor_url}\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("---\n\n")
            f.write(competitor_analysis)
        
        logger.info(f"Competitor analysis saved to {analysis_path}")
        
        return {
            "competitor_url": competitor_url,
            "analysis": competitor_analysis,
            "analysis_path": analysis_path
        }
    
    def generate_pillar_content(self, pillar_index):
        """Generate content for a specific content pillar."""
        if pillar_index < 0 or pillar_index >= len(self.content_pillars):
            logger.error(f"Invalid pillar index: {pillar_index}")
            return None
        
        pillar = self.content_pillars[pillar_index]
        logger.info(f"Generating pillar content for: {pillar}")
        
        # Load keywords for this pillar
        keywords_df = self._load_keywords()
        if not keywords_df.empty:
            pillar_keywords = keywords_df[keywords_df['pillar'] == pillar]
            if not pillar_keywords.empty:
                keywords = pillar_keywords['keyword'].tolist()[:15]  # Use top 15 keywords
            else:
                keywords = []
        else:
            keywords = []
        
        # If no keywords found, use default ones
        if not keywords:
            keywords = [
                pillar,
                "SMSTS course",
                "CITB SMSTS",
                "site management safety training"
            ]
        
        # Generate content
        return self.generate_content(pillar, pillar, keywords)
    
    def generate_all_pillar_content(self):
        """Generate content for all content pillars."""
        results = []
        
        for i, pillar in enumerate(self.content_pillars):
            result = self.generate_pillar_content(i)
            if result:
                results.append(result)
        
        return results
    
    def generate_location_content(self, location):
        """Generate location-specific content."""
        logger.info(f"Generating location content for: {location}")
        
        # Determine which pillar this belongs to
        pillar = "Navigating SMSTS Course Delivery and Providers"
        
        # Create topic
        topic = f"SMSTS Courses in {location}: Complete Guide"
        
        # Generate location-specific keywords
        keywords = [
            f"SMSTS course {location}",
            f"{location} SMSTS training",
            f"SMSTS course in {location}",
            f"SMSTS {location} weekend",
            f"CITB SMSTS {location}",
            f"book SMSTS course {location}"
        ]
        
        # Generate content
        return self.generate_content(topic, pillar, keywords)
    
    def generate_all_location_content(self, locations=None):
        """Generate content for all locations."""
        if not locations:
            locations = self.config.get("keyword_research", {}).get("locations", [])
        
        results = []
        
        for location in locations:
            result = self.generate_location_content(location)
            if result:
                results.append(result)
        
        return results


def main():
    """Main function to run the AI-enhanced content generator."""
    import argparse
    
    parser = argparse.ArgumentParser(description='AI-Enhanced Content Generator')
    parser.add_argument('--topic', help='Topic to generate content for')
    parser.add_argument('--pillar', help='Content pillar')
    parser.add_argument('--pillar-index', type=int, help='Content pillar index (0-4)')
    parser.add_argument('--location', help='Location to generate content for')
    parser.add_argument('--all-pillars', action='store_true', help='Generate content for all pillars')
    parser.add_argument('--all-locations', action='store_true', help='Generate content for all locations')
    parser.add_argument('--keywords', help='Comma-separated list of keywords')
    parser.add_argument('--analyze-keywords', help='Comma-separated list of keywords to analyze')
    parser.add_argument('--competitor-url', help='Competitor URL to analyze')
    parser.add_argument('--competitor-content-file', help='File containing competitor content to analyze')
    
    args = parser.parse_args()
    
    generator = AIEnhancedContentGenerator()
    
    if args.analyze_keywords:
        keywords = [k.strip() for k in args.analyze_keywords.split(',')]
        generator.analyze_keywords(keywords)
    
    elif args.competitor_url and args.competitor_content_file:
        with open(args.competitor_content_file, 'r', encoding='utf-8') as f:
            competitor_content = f.read()
        generator.analyze_competitor_content(args.competitor_url, competitor_content)
    
    elif args.all_pillars:
        generator.generate_all_pillar_content()
    
    elif args.all_locations:
        generator.generate_all_location_content()
    
    elif args.pillar_index is not None:
        generator.generate_pillar_content(args.pillar_index)
    
    elif args.location:
        generator.generate_location_content(args.location)
    
    elif args.topic and args.pillar:
        keywords = None
        if args.keywords:
            keywords = [k.strip() for k in args.keywords.split(',')]
        generator.generate_content(args.topic, args.pillar, keywords)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
