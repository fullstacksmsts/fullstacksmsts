#!/usr/bin/env python3
"""
AI Assistant Manager for fullstacksmsts.co.uk SEO Automation
This module integrates Claude 3 Sonnet and other AI assistants to enhance SEO capabilities.
"""

import os
import json
import time
import logging
import hashlib
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/ai_assistant.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('AI_Assistant_Manager')

class AIAssistantManager:
    """Manages different AI assistants for SEO tasks."""
    
    def __init__(self, config_file=None):
        """Initialize the AI assistant manager."""
        self.config_file = config_file or "config.json"
        self.config = self._load_config()
        
        # Set default assistant
        self.default_assistant = self.config.get("ai_assistant", {}).get("default", "claude")
        
        # Initialize assistants based on configuration
        self.assistants = {}
        
        # Initialize Claude if configured
        claude_config = self.config.get("ai_assistant", {}).get("claude")
        if claude_config:
            self.assistants["claude"] = ClaudeClient(claude_config)
        
        # Initialize other assistants if configured
        deepseek_config = self.config.get("ai_assistant", {}).get("deepseek")
        if deepseek_config:
            self.assistants["deepseek"] = DeepSeekClient(deepseek_config)
        
        gemini_config = self.config.get("ai_assistant", {}).get("gemini")
        if gemini_config:
            self.assistants["gemini"] = GeminiClient(gemini_config)
        
        # Load prompt templates
        self.prompt_templates = self._load_prompt_templates()
        
        # Initialize response cache
        self.cache_dir = "data/ai_cache"
        os.makedirs(self.cache_dir, exist_ok=True)
        
        logger.info(f"AI Assistant Manager initialized with {len(self.assistants)} assistants")
    
    def _load_config(self):
        """Load configuration from JSON file."""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            return config
        except Exception as e:
            logger.error(f"Error loading config: {str(e)}")
            return {}
    
    def _load_prompt_templates(self):
        """Load prompt templates for different SEO tasks."""
        templates_file = "scripts/ai_assistant/prompt_templates.json"
        try:
            if os.path.exists(templates_file):
                with open(templates_file, 'r') as f:
                    return json.load(f)
            else:
                logger.warning(f"Prompt templates file not found: {templates_file}")
                return self._create_default_templates()
        except Exception as e:
            logger.error(f"Error loading prompt templates: {str(e)}")
            return self._create_default_templates()
    
    def _create_default_templates(self):
        """Create default prompt templates."""
        templates = {
            "content_optimization": """
                Optimize the following content for SEO while maintaining readability and natural language flow.
                
                Target Keywords: {target_keywords}
                Content Pillar: {content_pillar}
                
                Original Content:
                {content}
                
                Please provide the optimized content with appropriate keyword placement, heading structure, 
                and internal linking opportunities. Ensure the content aligns with the specified content pillar.
            """,
            
            "keyword_analysis": """
                Analyze the following keywords for an SMSTS training provider website.
                
                Keywords: {keywords}
                
                For each keyword, provide:
                1. Search intent (informational, navigational, commercial, transactional)
                2. Relevance to SMSTS courses (high, medium, low)
                3. Content pillar alignment
                4. Suggested content type
                5. Recommended heading structure
            """,
            
            "competitor_analysis": """
                Analyze the following competitor content for an SMSTS training provider website.
                
                Competitor URL: {competitor_url}
                Competitor Content: {competitor_content}
                
                Please provide:
                1. Key topics covered
                2. Content structure analysis
                3. Keyword usage patterns
                4. Strengths and weaknesses
                5. Opportunities for our content to outperform this competitor
            """,
            
            "meta_description": """
                Create an SEO-optimized meta description for the following content.
                
                Target Keyword: {target_keyword}
                Content: {content}
                
                The meta description should:
                - Be between 150-160 characters
                - Include the target keyword naturally
                - Be compelling and encourage clicks
                - Accurately represent the content
                - Include a value proposition if possible
            """,
            
            "content_brief": """
                Create a detailed content brief for an article about {topic} for an SMSTS training provider website.
                
                Target Keywords: {target_keywords}
                Content Pillar: {content_pillar}
                
                The brief should include:
                1. Suggested title options (3-5)
                2. Meta description
                3. Target word count
                4. Heading structure (H1, H2, H3)
                5. Key points to cover
                6. Internal linking opportunities
                7. External reference suggestions
                8. Call-to-action recommendations
                
                Ensure the brief aligns with the content pillar and incorporates the target keywords naturally.
                Include our USPs: £360+VAT pricing, 98% pass rate, flexible scheduling options, and CITB accreditation.
            """,
            
            "technical_seo_analysis": """
                Analyze the following technical SEO issues and provide recommendations.
                
                Technical Issues: {technical_issues}
                
                For each issue, provide:
                1. Severity (critical, high, medium, low)
                2. Impact on SEO
                3. Step-by-step resolution instructions
                4. Expected outcome after fixing
            """
        }
        
        # Save default templates
        templates_file = "scripts/ai_assistant/prompt_templates.json"
        os.makedirs(os.path.dirname(templates_file), exist_ok=True)
        
        try:
            with open(templates_file, 'w') as f:
                json.dump(templates, f, indent=4)
            logger.info(f"Default prompt templates created at {templates_file}")
        except Exception as e:
            logger.error(f"Error saving default templates: {str(e)}")
        
        return templates
    
    def get_assistant(self, assistant_name=None):
        """Get the specified assistant or the default one."""
        name = assistant_name or self.default_assistant
        
        if name not in self.assistants:
            logger.error(f"Assistant '{name}' not configured, using default")
            name = self.default_assistant
            
            if name not in self.assistants:
                raise ValueError(f"Default assistant '{name}' not configured")
        
        return self.assistants[name]
    
    def execute_task(self, task_type, data, assistant_name=None):
        """Execute an AI task with the appropriate assistant."""
        # Generate cache key
        cache_key = self._generate_cache_key(task_type, data, assistant_name)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        # Check cache first
        cached_response = self._check_cache(cache_file)
        if cached_response:
            logger.info(f"Using cached response for task: {task_type}")
            return cached_response
        
        # Get the appropriate assistant
        try:
            assistant = self.get_assistant(assistant_name)
        except ValueError as e:
            logger.error(f"Error getting assistant: {str(e)}")
            return {"error": str(e)}
        
        # Get the prompt template for this task
        prompt_template = self.prompt_templates.get(task_type)
        if not prompt_template:
            error_msg = f"No prompt template found for task type '{task_type}'"
            logger.error(error_msg)
            return {"error": error_msg}
        
        # Format the prompt with the provided data
        try:
            prompt = prompt_template.format(**data)
        except KeyError as e:
            error_msg = f"Missing data for prompt template: {str(e)}"
            logger.error(error_msg)
            return {"error": error_msg}
        
        # Execute the task
        try:
            response = assistant.generate_response(prompt)
        except Exception as e:
            error_msg = f"Error generating response: {str(e)}"
            logger.error(error_msg)
            return {"error": error_msg}
        
        # Parse the response
        parsed_response = self._parse_response(response, task_type)
        
        # Cache the result
        self._cache_response(cache_file, parsed_response)
        
        return parsed_response
    
    def _generate_cache_key(self, task_type, data, assistant_name):
        """Generate a cache key for a task."""
        assistant = assistant_name or self.default_assistant
        data_str = json.dumps(data, sort_keys=True)
        hash_obj = hashlib.md5(data_str.encode())
        return f"{assistant}_{task_type}_{hash_obj.hexdigest()}"
    
    def _check_cache(self, cache_file):
        """Check if a cached response exists and is valid."""
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    cached_data = json.load(f)
                
                # Check if cache is expired (default: 7 days)
                cache_ttl = self.config.get("ai_assistant", {}).get("cache_ttl", 7 * 24 * 60 * 60)
                timestamp = cached_data.get("timestamp", 0)
                
                if time.time() - timestamp <= cache_ttl:
                    return cached_data.get("response")
            except Exception as e:
                logger.error(f"Error reading cache: {str(e)}")
        
        return None
    
    def _cache_response(self, cache_file, response):
        """Cache a response."""
        try:
            cache_data = {
                "timestamp": time.time(),
                "response": response
            }
            
            with open(cache_file, 'w') as f:
                json.dump(cache_data, f)
        except Exception as e:
            logger.error(f"Error caching response: {str(e)}")
    
    def _parse_response(self, response, task_type):
        """Parse the response based on task type."""
        # For now, return the raw response
        # In a more advanced implementation, this would parse the response into a structured format
        return {
            "task_type": task_type,
            "raw_response": response,
            "timestamp": datetime.now().isoformat()
        }
    
    def optimize_content(self, content, target_keywords, content_pillar):
        """Optimize content for SEO."""
        task_data = {
            "content": content,
            "target_keywords": ", ".join(target_keywords) if isinstance(target_keywords, list) else target_keywords,
            "content_pillar": content_pillar
        }
        
        result = self.execute_task("content_optimization", task_data)
        return result.get("raw_response") if "error" not in result else result.get("error")
    
    def analyze_keywords(self, keywords):
        """Analyze keywords for SEO."""
        task_data = {
            "keywords": ", ".join(keywords) if isinstance(keywords, list) else keywords
        }
        
        result = self.execute_task("keyword_analysis", task_data)
        return result.get("raw_response") if "error" not in result else result.get("error")
    
    def analyze_competitor(self, competitor_url, competitor_content):
        """Analyze competitor content."""
        task_data = {
            "competitor_url": competitor_url,
            "competitor_content": competitor_content
        }
        
        result = self.execute_task("competitor_analysis", task_data)
        return result.get("raw_response") if "error" not in result else result.get("error")
    
    def generate_meta_description(self, content, target_keyword):
        """Generate an SEO-optimized meta description."""
        # Truncate content to first 1000 characters for context
        content_preview = content[:1000] + ("..." if len(content) > 1000 else "")
        
        task_data = {
            "content": content_preview,
            "target_keyword": target_keyword
        }
        
        result = self.execute_task("meta_description", task_data)
        return result.get("raw_response") if "error" not in result else result.get("error")
    
    def create_content_brief(self, topic, target_keywords, content_pillar):
        """Create a content brief."""
        task_data = {
            "topic": topic,
            "target_keywords": ", ".join(target_keywords) if isinstance(target_keywords, list) else target_keywords,
            "content_pillar": content_pillar
        }
        
        result = self.execute_task("content_brief", task_data)
        return result.get("raw_response") if "error" not in result else result.get("error")
    
    def analyze_technical_issues(self, technical_issues):
        """Analyze technical SEO issues."""
        task_data = {
            "technical_issues": json.dumps(technical_issues) if isinstance(technical_issues, dict) else technical_issues
        }
        
        result = self.execute_task("technical_seo_analysis", task_data)
        return result.get("raw_response") if "error" not in result else result.get("error")


class ClaudeClient:
    """Client for Anthropic's Claude API."""
    
    def __init__(self, config):
        """Initialize the Claude client."""
        self.api_key = config.get("api_key") or os.getenv("CLAUDE_API_KEY")
        if not self.api_key:
            logger.error("Claude API key not found")
        
        self.model = config.get("model", "claude-3-sonnet-20240229")
        self.max_tokens = config.get("max_tokens", 4000)
        self.temperature = config.get("temperature", 0.7)
        
        logger.info(f"Claude client initialized with model: {self.model}")
    
    def generate_response(self, prompt, system_prompt=None):
        """Generate a response from Claude."""
        if not self.api_key:
            return "Error: Claude API key not configured"
        
        if not system_prompt:
            system_prompt = """You are an expert SEO assistant for fullstacksmsts.co.uk, a leading provider of online SMSTS courses. 
            Your task is to provide detailed, actionable SEO advice and analysis. 
            Focus on the five content pillars: Understanding CITB SMSTS Courses, Navigating SMSTS Course Delivery and Providers, 
            SMSTS Course Content and Assessment, SMSTS vs. Other Certifications, and Implementing SMSTS Knowledge on Site.
            
            Key information about fullstacksmsts.co.uk:
            - Offers CITB-accredited SMSTS courses priced at £360+VAT
            - Has a 98% pass rate for all courses
            - Provides flexible scheduling options (weekend, weekday, day release)
            - Offers translation services in any language
            
            Always provide practical, specific advice that can be implemented immediately."""
        
        try:
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }
            
            data = {
                "model": self.model,
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
                "system": system_prompt,
                "messages": [{"role": "user", "content": prompt}]
            }
            
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                return response.json()["content"][0]["text"]
            else:
                error_msg = f"Claude API error: {response.status_code} - {response.text}"
                logger.error(error_msg)
                return f"Error: {error_msg}"
        
        except Exception as e:
            error_msg = f"Error calling Claude API: {str(e)}"
            logger.error(error_msg)
            return f"Error: {error_msg}"


class DeepSeekClient:
    """Client for DeepSeek API."""
    
    def __init__(self, config):
        """Initialize the DeepSeek client."""
        self.api_key = config.get("api_key") or os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            logger.error("DeepSeek API key not found")
        
        self.model = config.get("model", "deepseek-r1-chat")
        self.max_tokens = config.get("max_tokens", 4000)
        self.temperature = config.get("temperature", 0.7)
        
        logger.info(f"DeepSeek client initialized with model: {self.model}")
    
    def generate_response(self, prompt, system_prompt=None):
        """Generate a response from DeepSeek."""
        if not self.api_key:
            return "Error: DeepSeek API key not configured"
        
        if not system_prompt:
            system_prompt = """You are an expert SEO assistant for fullstacksmsts.co.uk, a leading provider of online SMSTS courses. 
            Your task is to provide detailed, actionable SEO advice and analysis."""
        
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": self.max_tokens,
                "temperature": self.temperature
            }
            
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                error_msg = f"DeepSeek API error: {response.status_code} - {response.text}"
                logger.error(error_msg)
                return f"Error: {error_msg}"
        
        except Exception as e:
            error_msg = f"Error calling DeepSeek API: {str(e)}"
            logger.error(error_msg)
            return f"Error: {error_msg}"


class GeminiClient:
    """Client for Google's Gemini API."""
    
    def __init__(self, config):
        """Initialize the Gemini client."""
        self.api_key = config.get("api_key") or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.error("Gemini API key not found")
        
        self.model = config.get("model", "gemini-pro")
        self.max_tokens = config.get("max_tokens", 4000)
        self.temperature = config.get("temperature", 0.7)
        
        logger.info(f"Gemini client initialized with model: {self.model}")
    
    def generate_response(self, prompt, system_prompt=None):
        """Generate a response from Gemini."""
        if not self.api_key:
            return "Error: Gemini API key not configured"
        
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
            
            # Combine system prompt and user prompt if system prompt is provided
            content = prompt
            if system_prompt:
                content = f"{system_prompt}\n\n{prompt}"
            
            data = {
                "contents": [
                    {
                        "parts": [
                            {"text": content}
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": self.temperature,
                    "maxOutputTokens": self.max_tokens,
                    "topP": 0.95,
                    "topK": 40
                }
            }
            
            response = requests.post(url, json=data)
            
            if response.status_code == 200:
                return response.json()["candidates"][0]["content"]["parts"][0]["text"]
            else:
                error_msg = f"Gemini API error: {response.status_code} - {response.text}"
                logger.error(error_msg)
                return f"Error: {error_msg}"
        
        except Exception as e:
            error_msg = f"Error calling Gemini API: {str(e)}"
            logger.error(error_msg)
            return f"Error: {error_msg}"


def main():
    """Main function to test the AI Assistant Manager."""
    # Initialize the AI Assistant Manager
    manager = AIAssistantManager()
    
    # Test content optimization
    content = """
    SMSTS courses are essential for site managers in the construction industry. 
    These courses provide important safety training. 
    The CITB offers accreditation for SMSTS courses.
    """
    
    target_keywords = ["SMSTS course", "site management safety", "CITB accredited training"]
    content_pillar = "Understanding CITB SMSTS Courses"
    
    optimized_content = manager.optimize_content(content, target_keywords, content_pillar)
    print("\nOptimized Content:")
    print(optimized_content)
    
    # Test keyword analysis
    keywords = ["SMSTS course London", "weekend SMSTS training", "SMSTS online course price"]
    keyword_analysis = manager.analyze_keywords(keywords)
    print("\nKeyword Analysis:")
    print(keyword_analysis)
    
    # Test meta description generation
    meta_description = manager.generate_meta_description(content, "SMSTS course")
    print("\nMeta Description:")
    print(meta_description)


if __name__ == "__main__":
    main()
