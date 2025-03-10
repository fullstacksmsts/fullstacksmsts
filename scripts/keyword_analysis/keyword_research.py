#!/usr/bin/env python3
"""
Keyword Research Script for fullstacksmsts.co.uk
This script performs keyword research and analysis.
"""

import os
import re
import csv
import json
import logging
import argparse
import pandas as pd
import numpy as np
import random
from datetime import datetime
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Keyword_Research")

# Load environment variables
load_dotenv()

class KeywordResearcher:
    """Class to handle keyword research and analysis."""
    
    def __init__(self, seed_keywords=None, competitors=None, locations=None, output_file=None):
        """Initialize the keyword researcher."""
        self.seed_keywords = seed_keywords or []
        self.competitors = competitors or []
        self.locations = locations or []
        self.output_file = output_file or f"data/keywords/keyword_research_results_{datetime.now().strftime('%Y%m%d')}.xlsx"
        self.keywords = []
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
    
    def _generate_keyword_combinations(self):
        """Generate keyword combinations from seed keywords and modifiers."""
        logger.info("Generating keyword combinations...")
        
        # Basic combinations
        combinations = []
        for seed in self.seed_keywords:
            combinations.append(seed)
            
            # Add location-based keywords
            for location in self.locations:
                combinations.append(f"{seed} {location}")
                combinations.append(f"{location} {seed}")
                combinations.append(f"{seed} in {location}")
                combinations.append(f"{seed} near {location}")
            
            # Add common modifiers
            modifiers = [
                "online", "weekend", "cost", "price", "refresher",
                "certification", "exam", "test", "course dates",
                "near me", "training", "providers", "accredited",
                "cheap", "best", "top", "review", "reviews",
                "booking", "book", "register", "sign up", "enroll",
                "requirements", "duration", "length", "schedule",
                "syllabus", "content", "materials", "handbook",
                "pass rate", "success rate", "certificate", "qualification",
                "renewal", "refresher", "expiry", "validity"
            ]
            
            for modifier in modifiers:
                combinations.append(f"{seed} {modifier}")
                combinations.append(f"{modifier} {seed}")
            
            # Add question-based keywords
            questions = [
                "what is", "how to", "how much is", "where to",
                "when to", "why", "who needs", "is", "can", "does"
            ]
            
            for question in questions:
                combinations.append(f"{question} {seed}")
            
            # Add comparison keywords
            comparisons = [
                "vs", "versus", "or", "compared to", "alternative to",
                "difference between", "better than"
            ]
            
            comparison_terms = [
                "sssts", "cscs", "nebosh", "iosh", "citb",
                "nvq", "health and safety", "site safety",
                "construction safety", "site management"
            ]
            
            for comparison in comparisons:
                for term in comparison_terms:
                    combinations.append(f"{seed} {comparison} {term}")
                    combinations.append(f"{term} {comparison} {seed}")
        
        # Remove duplicates and clean up
        combinations = list(set(combinations))
        combinations = [kw.strip().lower() for kw in combinations if kw.strip()]
        
        logger.info(f"Generated {len(combinations)} keyword combinations.")
        return combinations
    
    def _simulate_keyword_metrics(self, keywords):
        """Simulate keyword metrics for demonstration purposes."""
        logger.info("Simulating keyword metrics...")
        
        # Create a DataFrame with the keywords
        df = pd.DataFrame({'keyword': keywords})
        
        # Simulate search volume
        # Higher volume for shorter, more generic keywords
        df['search_volume'] = df['keyword'].apply(
            lambda x: int(np.random.normal(
                loc=5000 / (len(x.split()) + 1),
                scale=1000 / (len(x.split()) + 1)
            ))
        )
        df['search_volume'] = df['search_volume'].apply(lambda x: max(10, x))
        
        # Simulate keyword difficulty (0-100)
        # Higher difficulty for shorter, more generic keywords
        df['difficulty'] = df['keyword'].apply(
            lambda x: min(100, max(1, int(np.random.normal(
                loc=80 / (len(x.split()) + 0.5),
                scale=15
            ))))
        )
        
        # Simulate cost per click (£)
        # Higher CPC for commercial intent keywords
        commercial_terms = ['course', 'training', 'certification', 'book', 'buy', 'register', 'sign up']
        df['cpc'] = df['keyword'].apply(
            lambda x: round(np.random.normal(
                loc=2.0 + sum(term in x for term in commercial_terms) * 0.5,
                scale=0.5
            ), 2)
        )
        df['cpc'] = df['cpc'].apply(lambda x: max(0.1, x))
        
        # Simulate current ranking (0 = not ranking, 1-100 = position)
        # Better rankings for brand terms and long-tail keywords
        brand_terms = ['fullstacksmsts', 'full stack smsts']
        df['current_rank'] = df['keyword'].apply(
            lambda x: int(np.random.normal(
                loc=50 - sum(term in x for term in brand_terms) * 30 - len(x.split()) * 3,
                scale=10
            )) if random.random() > 0.3 else 0
        )
        df['current_rank'] = df['current_rank'].apply(lambda x: min(100, max(0, x)))
        
        # Simulate monthly traffic potential
        # Based on search volume and current ranking
        df['traffic_potential'] = df.apply(
            lambda row: int(row['search_volume'] * (
                0.3 if row['current_rank'] <= 3 else
                0.15 if row['current_rank'] <= 10 else
                0.05 if row['current_rank'] <= 20 else
                0.01 if row['current_rank'] <= 50 else
                0.001 if row['current_rank'] <= 100 else
                0
            )), axis=1
        )
        
        # Simulate conversion potential (0-10)
        # Higher for commercial intent and branded keywords
        df['conversion_potential'] = df['keyword'].apply(
            lambda x: min(10, max(1, int(np.random.normal(
                loc=3 + sum(term in x for term in commercial_terms) * 1 + sum(term in x for term in brand_terms) * 2,
                scale=1
            ))))
        )
        
        # Assign content pillars
        pillar_assignments = {
            "Understanding CITB SMSTS Courses": [
                "what is smsts", "smsts meaning", "smsts course", "citb smsts", 
                "smsts certification", "smsts accreditation", "smsts qualification"
            ],
            "Navigating SMSTS Course Delivery and Providers": [
                "smsts course providers", "smsts training", "smsts course online",
                "weekend smsts course", "smsts course near me", "smsts course cost",
                "smsts course price", "smsts course dates", "book smsts", "smsts booking"
            ],
            "SMSTS Course Content and Assessment": [
                "smsts exam", "smsts test", "smsts course content",
                "smsts mock test", "smsts exam questions", "smsts pass rate",
                "smsts certificate", "smsts course duration", "smsts syllabus"
            ],
            "SMSTS vs. Other Certifications": [
                "smsts vs sssts", "smsts vs nebosh", "smsts vs iosh",
                "smsts equivalent", "smsts alternatives", "smsts or sssts",
                "construction safety certifications", "difference between smsts"
            ],
            "Implementing SMSTS Knowledge on Site": [
                "smsts site management", "applying smsts knowledge",
                "smsts best practices", "smsts site safety", "smsts responsibilities",
                "smsts risk assessment", "smsts method statements"
            ]
        }
        
        # Add pillar column
        df['pillar'] = ''
        
        # Assign pillars based on keyword matching
        for pillar, pillar_keywords in pillar_assignments.items():
            for pillar_keyword in pillar_keywords:
                mask = df['keyword'].str.contains(pillar_keyword, case=False, regex=False)
                df.loc[mask, 'pillar'] = pillar
        
        # Assign location keywords to the "Navigating SMSTS Course Delivery and Providers" pillar
        for location in self.locations:
            mask = df['keyword'].str.contains(location, case=False, regex=False)
            df.loc[mask, 'pillar'] = "Navigating SMSTS Course Delivery and Providers"
        
        # Default to first pillar for any remaining keywords
        df.loc[df['pillar'] == '', 'pillar'] = list(pillar_assignments.keys())[0]
        
        # Add journey stage column
        df['journey_stage'] = ''
        
        # Assign journey stages based on keyword intent
        awareness_keywords = ["what is", "meaning", "guide", "explained", "introduction", "basics"]
        consideration_keywords = ["compare", "vs", "versus", "difference", "review", "best", "top", "cost", "price"]
        conversion_keywords = ["book", "buy", "register", "sign up", "enroll", "course dates", "near me"]
        
        for keyword in awareness_keywords:
            mask = df['keyword'].str.contains(keyword, case=False, regex=False)
            df.loc[mask, 'journey_stage'] = "awareness"
        
        for keyword in consideration_keywords:
            mask = df['keyword'].str.contains(keyword, case=False, regex=False)
            df.loc[mask, 'journey_stage'] = "consideration"
        
        for keyword in conversion_keywords:
            mask = df['keyword'].str.contains(keyword, case=False, regex=False)
            df.loc[mask, 'journey_stage'] = "conversion"
        
        # Default to "consideration" for any remaining keywords
        df.loc[df['journey_stage'] == '', 'journey_stage'] = "consideration"
        
        # Add priority score (1-10)
        # Based on traffic potential, conversion potential, and difficulty
        df['priority_score'] = df.apply(
            lambda row: min(10, max(1, int(
                (row['traffic_potential'] / 100) * 0.4 +
                row['conversion_potential'] * 0.4 +
                (100 - row['difficulty']) / 10 * 0.2
            ))), axis=1
        )
        
        # Sort by priority score (descending)
        df = df.sort_values('priority_score', ascending=False)
        
        logger.info("Keyword metrics simulation completed.")
        return df
    
    def _analyze_competitors(self):
        """Analyze competitors' keywords."""
        logger.info("Analyzing competitors...")
        
        # In a real implementation, this would scrape competitor websites
        # or use SEO tools API to get competitor keywords
        # For this example, we'll generate some simulated competitor data
        
        competitor_keywords = []
        
        for competitor in self.competitors:
            # Simulate 20-50 keywords per competitor
            num_keywords = random.randint(20, 50)
            
            for _ in range(num_keywords):
                # Generate a random keyword from our seed keywords or combinations
                if random.random() < 0.7 and self.keywords:
                    # 70% chance to use one of our existing keywords
                    keyword = random.choice(self.keywords)
                else:
                    # 30% chance to generate a new keyword
                    base = random.choice(self.seed_keywords)
                    modifiers = [
                        "online", "weekend", "cost", "price", "refresher",
                        "certification", "exam", "test", "course dates",
                        "near me", "training", "providers", "accredited"
                    ]
                    modifier = random.choice(modifiers)
                    keyword = f"{base} {modifier}"
                
                # Add to competitor keywords
                competitor_keywords.append({
                    'competitor': competitor,
                    'keyword': keyword,
                    'rank': random.randint(1, 20),  # Simulate ranking position
                    'url': f"https://{competitor}/{keyword.replace(' ', '-')}"
                })
        
        # Convert to DataFrame
        df = pd.DataFrame(competitor_keywords)
        
        logger.info(f"Analyzed {len(self.competitors)} competitors, found {len(competitor_keywords)} keywords.")
        return df
    
    def _generate_keyword_recommendations(self, keywords_df, competitor_df):
        """Generate keyword recommendations based on analysis."""
        logger.info("Generating keyword recommendations...")
        
        # Identify high-opportunity keywords
        # High search volume, low difficulty, not ranking well
        high_opportunity = keywords_df[
            (keywords_df['search_volume'] > keywords_df['search_volume'].quantile(0.7)) &
            (keywords_df['difficulty'] < keywords_df['difficulty'].quantile(0.3)) &
            (keywords_df['current_rank'] > 10)
        ].copy()
        
        # Identify competitor gap keywords
        # Keywords where competitors rank well but we don't
        competitor_ranking = competitor_df.groupby('keyword')['rank'].min().reset_index()
        competitor_ranking = competitor_ranking[competitor_ranking['rank'] <= 10]
        
        competitor_gap = keywords_df[
            keywords_df['keyword'].isin(competitor_ranking['keyword']) &
            (keywords_df['current_rank'] > 20)
        ].copy()
        
        # Identify quick win keywords
        # Already ranking 11-20, moderate difficulty
        quick_win = keywords_df[
            (keywords_df['current_rank'] >= 11) &
            (keywords_df['current_rank'] <= 20) &
            (keywords_df['difficulty'] < keywords_df['difficulty'].quantile(0.5))
        ].copy()
        
        # Identify long-tail opportunities
        # Low competition, specific intent
        long_tail = keywords_df[
            (keywords_df['keyword'].str.split().str.len() >= 3) &
            (keywords_df['difficulty'] < keywords_df['difficulty'].quantile(0.3))
        ].copy()
        
        # Add recommendation type
        high_opportunity['recommendation_type'] = 'High Opportunity'
        competitor_gap['recommendation_type'] = 'Competitor Gap'
        quick_win['recommendation_type'] = 'Quick Win'
        long_tail['recommendation_type'] = 'Long-tail Opportunity'
        
        # Combine recommendations
        recommendations = pd.concat([
            high_opportunity,
            competitor_gap,
            quick_win,
            long_tail
        ]).drop_duplicates(subset=['keyword'])
        
        # Sort by priority score
        recommendations = recommendations.sort_values('priority_score', ascending=False)
        
        logger.info(f"Generated {len(recommendations)} keyword recommendations.")
        return recommendations
    
    def run(self):
        """Run the keyword research process."""
        logger.info("Starting keyword research process...")
        
        # Generate keyword combinations
        self.keywords = self._generate_keyword_combinations()
        
        # Simulate keyword metrics
        keywords_df = self._simulate_keyword_metrics(self.keywords)
        
        # Analyze competitors
        competitor_df = self._analyze_competitors()
        
        # Generate keyword recommendations
        recommendations_df = self._generate_keyword_recommendations(keywords_df, competitor_df)
        
        # Save results to Excel
        with pd.ExcelWriter(self.output_file) as writer:
            keywords_df.to_excel(writer, sheet_name='All Keywords', index=False)
            recommendations_df.to_excel(writer, sheet_name='Recommendations', index=False)
            competitor_df.to_excel(writer, sheet_name='Competitor Keywords', index=False)
            
            # Create a summary sheet
            summary_data = {
                'Metric': [
                    'Total Keywords Analyzed',
                    'High Opportunity Keywords',
                    'Competitor Gap Keywords',
                    'Quick Win Keywords',
                    'Long-tail Opportunity Keywords',
                    'Keywords Already Ranking Top 10',
                    'Keywords Ranking 11-20',
                    'Keywords Ranking 21-50',
                    'Keywords Not Ranking',
                    'Average Keyword Difficulty',
                    'Average Search Volume',
                    'Average CPC (£)',
                    'Estimated Monthly Traffic Potential'
                ],
                'Value': [
                    len(keywords_df),
                    len(recommendations_df[recommendations_df['recommendation_type'] == 'High Opportunity']),
                    len(recommendations_df[recommendations_df['recommendation_type'] == 'Competitor Gap']),
                    len(recommendations_df[recommendations_df['recommendation_type'] == 'Quick Win']),
                    len(recommendations_df[recommendations_df['recommendation_type'] == 'Long-tail Opportunity']),
                    len(keywords_df[keywords_df['current_rank'] <= 10]),
                    len(keywords_df[(keywords_df['current_rank'] > 10) & (keywords_df['current_rank'] <= 20)]),
                    len(keywords_df[(keywords_df['current_rank'] > 20) & (keywords_df['current_rank'] <= 50)]),
                    len(keywords_df[keywords_df['current_rank'] == 0]),
                    f"{keywords_df['difficulty'].mean():.1f}/100",
                    int(keywords_df['search_volume'].mean()),
                    f"£{keywords_df['cpc'].mean():.2f}",
                    int(keywords_df['traffic_potential'].sum())
                ]
            }
            
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='Summary', index=False)
            
            # Create a pillar content sheet
            pillar_data = keywords_df.groupby('pillar').agg({
                'keyword': 'count',
                'search_volume': 'sum',
                'traffic_potential': 'sum',
                'difficulty': 'mean'
            }).reset_index()
            
            pillar_data.columns = ['Content Pillar', 'Keyword Count', 'Total Search Volume', 'Traffic Potential', 'Average Difficulty']
            pillar_data.to_excel(writer, sheet_name='Content Pillars', index=False)
            
            # Create a journey stage sheet
            journey_data = keywords_df.groupby('journey_stage').agg({
                'keyword': 'count',
                'search_volume': 'sum',
                'traffic_potential': 'sum',
                'conversion_potential': 'mean'
            }).reset_index()
            
            journey_data.columns = ['Journey Stage', 'Keyword Count', 'Total Search Volume', 'Traffic Potential', 'Average Conversion Potential']
            journey_data.to_excel(writer, sheet_name='Journey Stages', index=False)
            
            # Create a location keywords sheet
            location_keywords = pd.DataFrame()
            for location in self.locations:
                location_df = keywords_df[keywords_df['keyword'].str.contains(location, case=False, regex=False)]
                if not location_df.empty:
                    location_df['location'] = location
                    location_keywords = pd.concat([location_keywords, location_df])
            
            if not location_keywords.empty:
                location_keywords.to_excel(writer, sheet_name='Location Keywords', index=False)
        
        logger.info(f"Keyword research completed successfully. Results saved to {self.output_file}")
        return self.output_file

def main(seed_keywords=None, competitors=None, locations=None, output_file=None):
    """Main function to run keyword research."""
    # Default seed keywords if not provided
    if not seed_keywords:
        seed_keywords = [
            "smsts course",
            "smsts training",
            "site management safety training scheme",
            "citb smsts",
            "smsts online"
        ]
    
    # Default competitors if not provided
    if not competitors:
        competitors = [
            "smsts-course.co.uk",
            "knightlearning.co.uk",
            "tamtraining.co.uk",
            "goldcrosstraining.co.uk",
            "3btraining.com"
        ]
    
    # Default locations if not provided
    if not locations:
        locations = [
            "London",
            "Manchester",
            "Birmingham",
            "Glasgow",
            "Leeds"
        ]
    
    # Create and run keyword researcher
    researcher = KeywordResearcher(seed_keywords, competitors, locations, output_file)
    return researcher.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keyword Research for fullstacksmsts.co.uk")
    parser.add_argument("--seed-keywords", nargs="+", help="Seed keywords")
    parser.add_argument("--competitors", nargs="+", help="Competitor domains")
    parser.add_argument("--locations", nargs="+", help="Target locations")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    main(args.seed_keywords, args.competitors, args.locations, args.output)
