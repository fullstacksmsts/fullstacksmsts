#!/usr/bin/env python3
"""
Location Page Generator Script for fullstacksmsts.co.uk
This script generates location-specific content based on templates and keyword data.
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
logger = logging.getLogger("Location_Page_Generator")

# Load environment variables
load_dotenv()

class LocationPageGenerator:
    """Class to handle location page generation."""
    
    def __init__(self, template_file, keywords_file, location, output_dir=None):
        """Initialize the location page generator."""
        self.template_file = template_file
        self.keywords_file = keywords_file
        self.location = location
        self.output_dir = output_dir or "output/content/locations"
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
    
    def _get_location_keywords(self):
        """Get keywords related to the location."""
        # Filter keywords containing the location name
        location_keywords = self.keywords_df[
            self.keywords_df['keyword'].str.contains(self.location, case=False)
        ]
        
        if location_keywords.empty:
            logger.warning(f"No keywords found for location: {self.location}")
            return []
        
        # Sort by priority (if available) or search volume
        if 'priority_score' in location_keywords.columns:
            location_keywords = location_keywords.sort_values('priority_score', ascending=False)
        elif 'search_volume' in location_keywords.columns:
            location_keywords = location_keywords.sort_values('search_volume', ascending=False)
        
        return location_keywords['keyword'].tolist()
    
    def _generate_venue_info(self):
        """Generate venue information for the location."""
        # Map of location-specific venue information
        venue_info = {
            "London": {
                "venue": "London SMSTS Training Centre",
                "address": "123 Safety Street, London, EC1A 1BB",
                "description": "Our London training venue is conveniently located in the heart of the city, just a 5-minute walk from Liverpool Street Station. The modern facility features comfortable classrooms, breakout areas, and all necessary amenities for a productive learning experience."
            },
            "Manchester": {
                "venue": "Manchester Construction Training Hub",
                "address": "456 Builder's Way, Manchester, M1 2AB",
                "description": "Located in central Manchester, our training facility is easily accessible by public transport and offers free parking for delegates. The purpose-built training rooms are equipped with the latest technology to enhance your learning experience."
            },
            "Birmingham": {
                "venue": "Birmingham Safety Centre",
                "address": "789 Construction Road, Birmingham, B1 1TF",
                "description": "Our Birmingham venue is situated in the city centre, close to New Street Station. The modern facility provides a comfortable learning environment with all the resources needed for your SMSTS course."
            },
            "Glasgow": {
                "venue": "Glasgow Construction Academy",
                "address": "101 Site Manager Street, Glasgow, G1 2CD",
                "description": "The Glasgow training centre is located just 10 minutes from Glasgow Central Station. Our purpose-built facility offers spacious classrooms, complimentary refreshments, and all the resources needed for effective SMSTS training."
            },
            "Leeds": {
                "venue": "Leeds Safety Training Centre",
                "address": "202 Management Avenue, Leeds, LS1 3EF",
                "description": "Our Leeds venue is conveniently located near the city centre with excellent transport links. The modern facility provides a comfortable and professional environment for your SMSTS training."
            }
        }
        
        # Get venue info for this location, or use generic info
        if self.location in venue_info:
            return venue_info[self.location]
        else:
            return {
                "venue": f"{self.location} SMSTS Training Centre",
                "address": f"123 Construction Street, {self.location}",
                "description": f"Our {self.location} training venue is conveniently located with good transport links. The facility provides a comfortable and professional environment for your SMSTS training, with all necessary resources and amenities."
            }
    
    def _generate_local_context(self):
        """Generate location-specific construction context."""
        # Map of location-specific construction context
        context_info = {
            "London": "London's construction industry is booming, with major projects including high-rise developments, infrastructure upgrades, and the ongoing transformation of areas like Nine Elms and Battersea. Site managers with SMSTS certification are in high demand across the capital, with opportunities in residential, commercial, and public sector projects. Our SMSTS courses in London are tailored to address the unique challenges of construction in a dense urban environment, including logistics, noise restrictions, and coordination with Transport for London.",
            
            "Manchester": "Manchester's construction sector continues to thrive, with significant development in areas like Salford Quays, NOMA, and Ancoats. The city's skyline is constantly evolving with new residential towers and commercial spaces. SMSTS-certified site managers are essential to Manchester's growth, managing complex projects in both new developments and heritage renovations. Our Manchester SMSTS courses incorporate local knowledge of the city's construction landscape and regulatory environment.",
            
            "Birmingham": "Birmingham is experiencing unprecedented growth in construction, with the HS2 project, Paradise development, and numerous residential schemes transforming the city. The Big City Plan continues to drive investment in infrastructure and buildings. SMSTS-qualified managers are crucial to delivering these projects safely and efficiently. Our Birmingham SMSTS courses address the specific challenges of working in the UK's second-largest city, including urban regeneration projects and mixed-use developments.",
            
            "Glasgow": "Glasgow's construction industry is vibrant, with significant investment in residential developments, commercial properties, and infrastructure projects. The city's rich architectural heritage presents unique challenges for construction professionals, balancing preservation with modernization. SMSTS certification is highly valued by Glasgow employers, particularly for projects involving historic buildings or complex urban sites. Our Glasgow SMSTS courses incorporate understanding of local building regulations and Scottish construction practices.",
            
            "Leeds": "Leeds is experiencing a construction boom, with major developments like SOYO, Wellington Place, and South Bank transforming the city. The demand for qualified site managers with SMSTS certification continues to grow across Yorkshire. Our Leeds SMSTS courses address the specific needs of the regional construction industry, from city centre high-rise projects to suburban developments and infrastructure works across West Yorkshire."
        }
        
        # Get context for this location, or use generic info
        if self.location in context_info:
            return context_info[self.location]
        else:
            return f"The construction industry in {self.location} offers numerous opportunities for qualified site managers with SMSTS certification. Local projects range from residential and commercial developments to infrastructure improvements. Our {self.location} SMSTS courses are designed to prepare you for the specific challenges and requirements of construction projects in this area, ensuring you have the knowledge and skills to manage sites safely and effectively."
    
    def _generate_testimonials(self):
        """Generate location-specific testimonials."""
        # Generic testimonials that can be adapted to any location
        testimonials = [
            {
                "name": "John Smith",
                "role": "Site Manager",
                "company": "ABC Construction Ltd",
                "text": f"Taking my SMSTS course with fullstacksmsts.co.uk in {self.location} was one of the best career decisions I've made. The trainers were knowledgeable and experienced, and the course content was directly applicable to my daily work. I passed first time and have already recommended the course to my colleagues."
            },
            {
                "name": "Sarah Johnson",
                "role": "Project Manager",
                "company": "XYZ Developments",
                "text": f"I needed to renew my SMSTS certificate and chose the weekend course in {self.location} to avoid taking time off work. The flexible scheduling was perfect, and the quality of training was excellent. The venue was comfortable and conveniently located. I particularly appreciated the practical examples relevant to construction in {self.location}."
            },
            {
                "name": "Mohammed Patel",
                "role": "Construction Supervisor",
                "company": "Buildwell Construction",
                "text": f"As someone who speaks English as a second language, I was concerned about the SMSTS course. fullstacksmsts.co.uk provided translation assistance during my course in {self.location}, which made a huge difference. The trainers were patient and supportive, and I'm proud to say I passed with flying colors."
            }
        ]
        
        # Format testimonials as HTML
        testimonials_html = ""
        for testimonial in testimonials:
            testimonials_html += f"""
<div class="testimonial">
    <blockquote>"{testimonial['text']}"</blockquote>
    <p class="testimonial-author">- {testimonial['name']}, {testimonial['role']} at {testimonial['company']}</p>
</div>
"""
        
        return testimonials_html
    
    def _generate_faqs(self):
        """Generate location-specific FAQs."""
        # Generic FAQs that can be adapted to any location
        faqs = [
            {
                "question": f"Where exactly is the SMSTS course held in {self.location}?",
                "answer": f"Our SMSTS courses in {self.location} are held at {self._generate_venue_info()['venue']}, located at {self._generate_venue_info()['address']}. The venue is easily accessible by public transport and has parking facilities available for delegates."
            },
            {
                "question": f"How often do you run SMSTS courses in {self.location}?",
                "answer": f"We run SMSTS courses in {self.location} regularly throughout the year. Typically, we offer weekday courses every month and weekend courses every 6-8 weeks. Please contact us for the most up-to-date schedule or to request a specific date."
            },
            {
                "question": f"Is the {self.location} SMSTS course exactly the same as courses in other locations?",
                "answer": f"The core SMSTS curriculum is standardized across all locations as per CITB requirements. However, our {self.location} courses include local context and examples relevant to construction projects in the area. All our courses, regardless of location, are CITB-accredited and have the same 98% pass rate."
            },
            {
                "question": f"Do you offer in-house SMSTS training for companies in {self.location}?",
                "answer": f"Yes, we can arrange in-house SMSTS training for companies in {self.location} with a minimum of 6 delegates. This can be more cost-effective and convenient for your team. Contact us to discuss your specific requirements and to schedule in-house training at your premises or a location of your choice."
            },
            {
                "question": f"What if I need to reschedule my SMSTS course in {self.location}?",
                "answer": f"We understand that plans can change. You can reschedule your {self.location} SMSTS course up to 10 working days before the start date without any additional cost. For changes made less than 10 working days before the course, a small administrative fee may apply. Please contact us as soon as possible if you need to reschedule."
            }
        ]
        
        # Format FAQs as HTML
        faqs_html = ""
        for faq in faqs:
            faqs_html += f"""
<div class="faq-item">
    <h3 class="faq-question">{faq['question']}</h3>
    <p class="faq-answer">{faq['answer']}</p>
</div>
"""
        
        return faqs_html
    
    def generate_location_page(self):
        """Generate a location-specific page."""
        logger.info(f"Generating location page for {self.location}...")
        
        # Load template and keywords
        if not self._load_template() or not self._load_keywords():
            return False
        
        # Get location-specific keywords
        location_keywords = self._get_location_keywords()
        
        # Get venue information
        venue_info = self._generate_venue_info()
        
        # Generate content variables
        content_vars = {
            'location': self.location,
            'venue': venue_info['venue'],
            'address': venue_info['address'],
            'intro': f"Looking for an SMSTS course in {self.location}? fullstacksmsts.co.uk offers CITB-accredited Site Management Safety Training Scheme courses in {self.location} with a 98% pass rate. Our flexible scheduling options include weekday, weekend, and online courses, all priced at £360+VAT. We also provide translation services in any language to ensure accessibility for all construction professionals.",
            'why_section': f"Taking your SMSTS course in {self.location} with fullstacksmsts.co.uk offers numerous benefits. Our courses are fully accredited by the Construction Industry Training Board (CITB), ensuring your certification is recognized industry-wide. With a 98% pass rate, our experienced trainers provide expert guidance throughout the 5-day course. We offer flexible scheduling options to suit your work commitments, including weekday courses, weekend courses, and day release options. Our {self.location} training venue is conveniently located and provides a comfortable learning environment.",
            'weekday_courses': f"Our standard weekday SMSTS courses in {self.location} run Monday to Friday from 9:00 AM to 5:00 PM. This intensive format allows you to complete your training in one consecutive week, minimizing disruption to your work schedule. Courses are held at our {venue_info['venue']} and include all necessary materials, refreshments, and certification fees.",
            'weekend_courses': f"For those unable to attend during the week, our weekend SMSTS courses in {self.location} provide a flexible alternative. These courses run over three consecutive weekends (Saturday and Sunday), allowing you to balance your training with work commitments. The weekend format is particularly popular with working site managers and those traveling from outside {self.location}.",
            'day_release_courses': f"Our day release SMSTS courses in {self.location} are spread over five weeks, with one full day of training per week. This format is ideal for those who cannot commit to a full week of training but prefer not to train on weekends. Day release courses are typically held on the same day each week (e.g., every Tuesday) at our {venue_info['venue']}.",
            'online_courses': f"In addition to our in-person training options, we offer fully accredited online SMSTS courses for {self.location}-based construction professionals. These courses follow the same curriculum and result in the same CITB certification as our classroom courses. Online courses combine live virtual classroom sessions with self-paced learning, providing maximum flexibility while maintaining interactive learning and instructor support.",
            'venue_info': venue_info['description'],
            'course_content': "The SMSTS course covers essential site management safety topics including health and safety law, CDM regulations, risk assessment, method statements, behavioral safety, occupational health, and site set-up. The course is assessed through a multiple-choice test and a practical site management project. Upon successful completion, you'll receive a CITB Site Safety Plus certificate valid for 5 years.",
            'local_context': self._generate_local_context(),
            'testimonials': self._generate_testimonials(),
            'faqs': self._generate_faqs(),
            'cta': f"Ready to book your SMSTS course in {self.location}? Contact fullstacksmsts.co.uk today to secure your place on our next available course. With our 98% pass rate, flexible scheduling options, and competitive price of £360+VAT, you'll be on your way to becoming a qualified site manager or supervisor. We also offer translation services in any language to ensure all construction professionals can access our training. Don't delay – SMSTS certification is your pathway to enhanced career opportunities and safer construction sites in {self.location} and beyond."
        }
        
        # Generate content using template
        try:
            content = self.template.substitute(content_vars)
            
            # Create filename
            filename = f"smsts-course-{self.location.lower()}.md"
            output_path = os.path.join(self.output_dir, filename)
            
            # Save content
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Location page for {self.location} saved to {output_path}")
            return True
        except KeyError as e:
            logger.error(f"Missing template variable: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Error generating location page: {str(e)}")
            return False

def main(template_file=None, keywords_file=None, location=None, output_dir=None):
    """Main function to run location page generation."""
    # Default files if not provided
    if not template_file:
        template_file = "templates/location_pages/location_page_template.md"
    
    if not keywords_file:
        keywords_file = "data/keywords/location_keywords.csv"
    
    if not location:
        logger.error("Location must be specified.")
        return False
    
    # Create and run location page generator
    generator = LocationPageGenerator(template_file, keywords_file, location, output_dir)
    return generator.generate_location_page()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Location Page Generator for fullstacksmsts.co.uk")
    parser.add_argument("--template", help="Template file path")
    parser.add_argument("--keywords", help="Keywords file path")
    parser.add_argument("--location", required=True, help="Location name")
    parser.add_argument("--output", help="Output directory path")
    
    args = parser.parse_args()
    main(args.template, args.keywords, args.location, args.output)
