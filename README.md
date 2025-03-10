# FullStack SMSTS Website and SEO Automation

This repository contains the code for the FullStack SMSTS website (https://fullstacksmsts.co.uk) and SEO automation tools.

## Project Structure

```
├── src/
│   ├── components/
│   │   └── blog/
│   │       ├── BlogPost.jsx         # Main blog post component
│   │       ├── RelatedPosts.jsx     # Related posts component
│   │       └── CommentSection.jsx   # Comment section component
│   ├── data/
│   │   └── blogPosts.js             # Mock blog post data
│   └── scripts/
│       ├── seoMonitor.js            # SEO monitoring system
│       └── masterAutomation.js      # Master SEO automation script
├── scripts/                         # Python SEO automation scripts
│   ├── ai_assistant/
│   ├── content_generation/
│   ├── keyword_analysis/
│   ├── reporting/
│   └── technical_seo/
└── templates/                       # Templates for content generation
    ├── blog_posts/
    ├── location_pages/
    └── reporting/
```

## Features

### Blog System

- Responsive blog post pages with SEO optimization
- Structured data for rich search results
- Related posts functionality
- Comment system
- Call-to-action sections

### SEO Automation

- Keyword research automation
- Technical SEO auditing
- Content generation
- Competitor analysis
- SEO monitoring
- Reporting

## React Blog Components

The blog system is built with React and includes the following components:

- **BlogPost**: Main component for displaying blog posts
- **RelatedPosts**: Component for displaying related articles
- **CommentSection**: Component for the comment form and display

## SEO Automation Scripts

The SEO automation system includes:

- **SEO Monitor**: Monitors keyword rankings, website traffic, and competitor changes
- **Master Automation**: Orchestrates all SEO tasks in a single workflow

## Getting Started

### Prerequisites

- Node.js (v14+)
- Python (v3.8+)
- Required npm packages (React, React Router, etc.)
- Required Python packages (see requirements.txt)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/fullstacksmsts/fullstacksmsts.git
   cd fullstacksmsts
   ```

2. Install JavaScript dependencies:
   ```
   npm install
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Blog System

```
npm start
```

### Running SEO Automation

```
python master_automation.py
```

## SEO Strategy

The SEO strategy focuses on five main content pillars:

1. Understanding CITB SMSTS Courses
2. Navigating SMSTS Course Delivery and Providers
3. SMSTS Course Content and Assessment
4. SMSTS vs. Other Certifications
5. Implementing SMSTS Knowledge on Site

## License

Proprietary - All rights reserved

## Contact

For inquiries, please contact info@fullstacksmsts.co.uk
