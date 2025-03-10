#!/usr/bin/env python3
"""
Content Generator Script for fullstacksmsts.co.uk
This script generates content based on templates and keyword data.
"""

import os
import logging
import argparse
import pandas as pd
import random
from string import Template
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Content_Generator")

# Load environment variables
load_dotenv()

class ContentGenerator:
    """Class to handle content generation."""
    
    def __init__(self, template_file, keywords_file, output_dir=None):
        """Initialize the content generator."""
        self.template_file = template_file
        self.keywords_file = keywords_file
        self.output_dir = output_dir or "output/content"
        self.template = None
        self.keywords_df = None
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _load_template(self):
        """Load the content template."""
        logger.info(f"Loading template from {self.template_file}")
        
        try:
            with open(self.template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()
            
            self.template = Template(template_content)
            logger.info("Template loaded successfully.")
            return True
        except Exception as e:
            logger.error(f"Error loading template: {str(e)}")
            return False
    
    def _load_keywords(self):
        """Load keyword data."""
        logger.info(f"Loading keywords from {self.keywords_file}")
        
        try:
            # Determine file type based on extension
            if self.keywords_file.endswith('.xlsx'):
                self.keywords_df = pd.read_excel(self.keywords_file)
            elif self.keywords_file.endswith('.csv'):
                self.keywords_df = pd.read_csv(self.keywords_file)
            else:
                logger.error(f"Unsupported file format: {self.keywords_file}")
                return False
            
            logger.info(f"Loaded {len(self.keywords_df)} keywords.")
            return True
        except Exception as e:
            logger.error(f"Error loading keywords: {str(e)}")
            return False
    
    def _generate_pillar_content(self, pillar):
        """Generate content for a specific pillar."""
        logger.info(f"Generating content for pillar: {pillar}")
        
        # Filter keywords for this pillar
        pillar_keywords = self.keywords_df[self.keywords_df['pillar'] == pillar]
        
        if pillar_keywords.empty:
            logger.warning(f"No keywords found for pillar: {pillar}")
            return None
        
        # Sort by priority (if available) or search volume
        if 'priority_score' in pillar_keywords.columns:
            pillar_keywords = pillar_keywords.sort_values('priority_score', ascending=False)
        elif 'search_volume' in pillar_keywords.columns:
            pillar_keywords = pillar_keywords.sort_values('search_volume', ascending=False)
        
        # Get top keywords for this pillar
        top_keywords = pillar_keywords.head(10)['keyword'].tolist()
        
        # Generate content variables
        content_vars = {
            'title': f"{pillar} - SMSTS Course Guide",
            'title_tag': f"{pillar} | SMSTS Course Guide | fullstacksmsts.co.uk",
            'meta_description': f"Comprehensive guide to {pillar.lower()}. Learn about CITB SMSTS courses, certification, and training options. £360+VAT with 98% pass rate.",
            'h1': pillar,
            'intro': self._generate_intro(pillar, top_keywords),
            'h2_1': self._generate_h2(pillar, 1),
            'body': self._generate_section(pillar, top_keywords, 1),
            'h2_2': self._generate_h2(pillar, 2),
            'section_2': self._generate_section(pillar, top_keywords, 2),
            'h2_3': self._generate_h2(pillar, 3),
            'section_3': self._generate_section(pillar, top_keywords, 3),
            'h2_4': self._generate_h2(pillar, 4),
            'section_4': self._generate_section(pillar, top_keywords, 4),
            'h2_5': self._generate_h2(pillar, 5),
            'conclusion': self._generate_conclusion(pillar, top_keywords),
            'faq_1_question': self._generate_faq_question(pillar, 1),
            'faq_1_answer': self._generate_faq_answer(pillar, 1),
            'faq_2_question': self._generate_faq_question(pillar, 2),
            'faq_2_answer': self._generate_faq_answer(pillar, 2),
            'faq_3_question': self._generate_faq_question(pillar, 3),
            'faq_3_answer': self._generate_faq_answer(pillar, 3),
            'faq_4_question': self._generate_faq_question(pillar, 4),
            'faq_4_answer': self._generate_faq_answer(pillar, 4),
            'faq_5_question': self._generate_faq_question(pillar, 5),
            'faq_5_answer': self._generate_faq_answer(pillar, 5),
            'cta': self._generate_cta(pillar)
        }
        
        # Generate content using template
        try:
            content = self.template.substitute(content_vars)
            return content
        except KeyError as e:
            logger.error(f"Missing template variable: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error generating content: {str(e)}")
            return None
    
    def _generate_intro(self, pillar, keywords):
        """Generate introduction section."""
        # In a real implementation, this would use NLP or AI to generate content
        # For this example, we'll use a template with some randomization
        
        intros = [
            f"Welcome to our comprehensive guide on {pillar.lower()}. This article provides essential information for construction professionals seeking to understand SMSTS certification and training options. At fullstacksmsts.co.uk, we offer CITB-accredited SMSTS courses with a 98% pass rate, flexible scheduling options including weekends and weekdays, and translation services in any language.",
            
            f"Understanding {pillar.lower()} is crucial for construction site managers and supervisors. This guide covers everything you need to know about SMSTS courses, certification requirements, and how to apply your knowledge on site. Our SMSTS courses are priced at £360+VAT, with online, weekend, and weekday options available to suit your schedule.",
            
            f"In this comprehensive guide to {pillar.lower()}, we'll explore the key aspects of SMSTS certification and training. As a leading provider of CITB-accredited SMSTS courses with a 98% success rate, fullstacksmsts.co.uk offers flexible course options including online delivery, weekend courses, and weekday training, all with translation services available in any language."
        ]
        
        return random.choice(intros)
    
    def _generate_h2(self, pillar, section_num):
        """Generate H2 heading."""
        # Map of pillar-specific headings
        pillar_headings = {
            "Understanding CITB SMSTS Courses": [
                "What is an SMSTS Course?",
                "CITB Accreditation and Why It Matters",
                "Who Needs an SMSTS Certificate?",
                "The Benefits of SMSTS Certification",
                "SMSTS Course Structure and Content"
            ],
            "Navigating SMSTS Course Delivery and Providers": [
                "Choosing the Right SMSTS Course Provider",
                "Online vs. In-Person SMSTS Courses",
                "Weekend and Flexible SMSTS Course Options",
                "SMSTS Course Pricing and Value",
                "What to Expect on Your SMSTS Course Day"
            ],
            "SMSTS Course Content and Assessment": [
                "Key Topics Covered in SMSTS Courses",
                "The SMSTS Assessment Process",
                "Tips for Passing Your SMSTS Exam",
                "Common SMSTS Test Questions",
                "What Happens After You Pass Your SMSTS"
            ],
            "SMSTS vs. Other Certifications": [
                "SMSTS vs. SSSTS: Understanding the Differences",
                "SMSTS vs. NEBOSH: Which is Right for You?",
                "How SMSTS Compares to IOSH Managing Safely",
                "The Construction Certification Hierarchy",
                "Combining SMSTS with Other Qualifications"
            ],
            "Implementing SMSTS Knowledge on Site": [
                "Applying SMSTS Principles on Construction Sites",
                "SMSTS and Legal Compliance",
                "Risk Assessment and Method Statements",
                "Managing Health and Safety Documentation",
                "Leadership Skills for SMSTS Certificate Holders"
            ]
        }
        
        # Get headings for this pillar, or use generic ones
        headings = pillar_headings.get(pillar, [
            f"Key Aspects of {pillar}",
            f"Important Considerations for {pillar}",
            f"Best Practices in {pillar}",
            f"Common Challenges in {pillar}",
            f"Future Trends in {pillar}"
        ])
        
        # Return the heading for the requested section
        if 0 <= section_num - 1 < len(headings):
            return headings[section_num - 1]
        else:
            return f"Section {section_num}: {pillar}"
    
    def _generate_section(self, pillar, keywords, section_num):
        """Generate a content section."""
        # In a real implementation, this would use NLP or AI to generate content
        # For this example, we'll use placeholder text
        
        paragraphs = [
            f"This section provides detailed information about {keywords[section_num % len(keywords)] if keywords else pillar}. Construction site managers and supervisors will find valuable insights into SMSTS certification requirements and best practices. Our CITB-accredited courses ensure you receive the most up-to-date training.",
            
            f"When considering {keywords[(section_num + 1) % len(keywords)] if keywords else pillar}, it's important to understand how this relates to overall site safety management. fullstacksmsts.co.uk offers comprehensive training with a 98% pass rate, ensuring you're well-prepared for your role as a site manager or supervisor.",
            
            f"Many construction professionals ask about {keywords[(section_num + 2) % len(keywords)] if keywords else pillar}. This is a critical aspect of site management safety training. Our courses are available in flexible formats including online, weekend, and weekday options, all priced at £360+VAT."
        ]
        
        return "\n\n".join(paragraphs)
    
    def _generate_conclusion(self, pillar, keywords):
        """Generate conclusion section."""
        return f"In conclusion, understanding {pillar.lower()} is essential for construction site managers and supervisors. By obtaining your SMSTS certification through fullstacksmsts.co.uk, you'll gain the knowledge and skills needed to ensure site safety and compliance with regulations. Our CITB-accredited courses offer flexible scheduling options, a 98% pass rate, and translation services in any language, all at a competitive price of £360+VAT."
    
    def _generate_faq_question(self, pillar, num):
        """Generate FAQ question."""
        # Map of pillar-specific FAQ questions
        pillar_questions = {
            "Understanding CITB SMSTS Courses": [
                "How long is an SMSTS certificate valid for?",
                "Is SMSTS certification a legal requirement for site managers?",
                "What is the difference between SMSTS and SSSTS?",
                "Can I take an SMSTS course online?",
                "How much does an SMSTS course cost?"
            ],
            "Navigating SMSTS Course Delivery and Providers": [
                "Are weekend SMSTS courses available?",
                "How do I choose a reputable SMSTS course provider?",
                "Can I get SMSTS training in languages other than English?",
                "What happens if I fail my SMSTS test?",
                "How far in advance should I book my SMSTS course?"
            ],
            "SMSTS Course Content and Assessment": [
                "What topics are covered in the SMSTS exam?",
                "How is the SMSTS course assessed?",
                "What is the pass rate for SMSTS courses?",
                "Are there practice tests available for SMSTS?",
                "How should I prepare for my SMSTS course?"
            ],
            "SMSTS vs. Other Certifications": [
                "Do I need both SMSTS and NEBOSH qualifications?",
                "Which is more valuable: SMSTS or IOSH Managing Safely?",
                "Can SSSTS holders progress to SMSTS?",
                "Is SMSTS recognized internationally?",
                "Which certification is best for career advancement in construction?"
            ],
            "Implementing SMSTS Knowledge on Site": [
                "How does SMSTS training improve site safety?",
                "What documentation should an SMSTS certificate holder maintain?",
                "How can I apply SMSTS principles to my specific construction site?",
                "What are the legal responsibilities of an SMSTS-certified manager?",
                "How does SMSTS training help with risk assessment?"
            ]
        }
        
        # Get questions for this pillar, or use generic ones
        questions = pillar_questions.get(pillar, [
            f"What are the key benefits of {pillar}?",
            f"How does {pillar} impact construction site safety?",
            f"Is {pillar} required for all construction projects?",
            f"How often should {pillar} be reviewed and updated?",
            f"What resources are available for learning more about {pillar}?"
        ])
        
        # Return the question for the requested number
        if 0 <= num - 1 < len(questions):
            return questions[num - 1]
        else:
            return f"What is important to know about {pillar}?"
    
    def _generate_faq_answer(self, pillar, num):
        """Generate FAQ answer."""
        # In a real implementation, this would use NLP or AI to generate content
        # For this example, we'll use placeholder text
        
        return f"This is an important question about {pillar.lower()}. At fullstacksmsts.co.uk, we provide comprehensive SMSTS training that addresses this and many other questions. Our CITB-accredited courses have a 98% pass rate and are available in flexible formats including online, weekend, and weekday options, all priced at £360+VAT. We also offer translation services in any language to ensure all construction professionals can access our training."
    
    def _generate_cta(self, pillar):
        """Generate call to action."""
        return f"Ready to advance your construction career with SMSTS certification? Book your {pillar.lower()} course today with fullstacksmsts.co.uk. With our 98% pass rate, flexible scheduling options, and competitive price of £360+VAT, you'll be on your way to becoming a qualified site manager or supervisor. Contact us now to discuss your training needs or to arrange translation services in your preferred language."
    
    def generate_content(self):
        """Generate content for all pillars."""
        logger.info("Starting content generation process...")
        
        # Load template and keywords
        if not self._load_template() or not self._load_keywords():
            return False
        
        # Get unique pillars
        if 'pillar' not in self.keywords_df.columns:
            logger.error("Keyword data does not contain 'pillar' column.")
            return False
        
        pillars = self.keywords_df['pillar'].unique()
        
        # Generate content for each pillar
        for pillar in pillars:
            logger.info(f"Processing pillar: {pillar}")
            
            # Skip empty pillars
            if not pillar or pd.isna(pillar):
                continue
            
            # Generate content
            content = self._generate_pillar_content(pillar)
            if not content:
                logger.warning(f"Failed to generate content for pillar: {pillar}")
                continue
            
            # Create filename
            filename = f"{pillar.lower().replace(' ', '-')}.md"
            output_path = os.path.join(self.output_dir, filename)
            
            # Save content
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                logger.info(f"Content saved to {output_path}")
            except Exception as e:
                logger.error(f"Error saving content: {str(e)}")
        
        logger.info("Content generation completed.")
        return True

def main(template_file=None, keywords_file=None, output_dir=None):
    """Main function to run content generation."""
    # Default files if not provided
    if not template_file:
        template_file = "templates/blog_posts/pillar_content_template.md"
    
    if not keywords_file:
        keywords_file = "data/keywords/keyword_research_results.xlsx"
    
    # Create and run content generator
    generator = ContentGenerator(template_file, keywords_file, output_dir)
    return generator.generate_content()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Content Generator for fullstacksmsts.co.uk")
    parser.add_argument("--template", help="Template file path")
    parser.add_argument("--keywords", help="Keywords file path")
    parser.add_argument("--output", help="Output directory path")
    
    args = parser.parse_args()
    main(args.template, args.keywords, args.output)
