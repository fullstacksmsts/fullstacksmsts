# FullStack SMSTS Website and SEO Automation

This repository contains the code for the FullStack SMSTS website (https://fullstacksmsts.co.uk) and SEO automation tools.

## Project Structure

```
├── public/                          # Public assets
│   ├── index.html                   # HTML entry point
│   ├── manifest.json                # Web app manifest
│   └── robots.txt                   # Robots configuration
├── src/
│   ├── components/
│   │   ├── blog/
│   │   │   ├── BlogPost.jsx         # Main blog post component
│   │   │   ├── BlogList.jsx         # Blog listing component
│   │   │   ├── RelatedPosts.jsx     # Related posts component
│   │   │   └── CommentSection.jsx   # Comment section component
│   │   ├── layout/
│   │   │   ├── Layout.jsx           # Main layout wrapper
│   │   │   ├── Header.jsx           # Site header
│   │   │   ├── Navigation.jsx       # Navigation menu
│   │   │   └── Footer.jsx           # Site footer
│   │   └── pages/
│   │       ├── HomePage.jsx         # Home page component
│   │       └── NotFoundPage.jsx     # 404 page component
│   ├── data/
│   │   └── blogPosts.js             # Mock blog post data
│   ├── scripts/
│   │   ├── seoMonitor.js            # SEO monitoring system
│   │   └── masterAutomation.js      # Master SEO automation script
│   ├── App.js                       # Main App component with routing
│   ├── index.js                     # JavaScript entry point
│   └── index.css                    # Global styles with Tailwind
├── scripts/                         # Python SEO automation scripts
│   ├── ai_assistant/
│   ├── content_generation/
│   ├── keyword_analysis/
│   ├── reporting/
│   └── technical_seo/
├── templates/                       # Templates for content generation
│   ├── blog_posts/
│   ├── location_pages/
│   └── reporting/
├── package.json                     # Project dependencies
├── tailwind.config.js               # Tailwind CSS configuration
└── postcss.config.js                # PostCSS configuration
```

## Features

### Blog System

- Responsive blog post pages with SEO optimization
- Blog listing page with featured post
- Structured data for rich search results
- Related posts functionality
- Comment system
- Call-to-action sections
- Mobile-friendly design with Tailwind CSS

### Website Features

- Responsive layout with mobile-first design
- SEO-optimized with proper meta tags and structured data
- Accessible navigation with keyboard support
- Fast loading with optimized assets
- Clear call-to-actions for course bookings

### SEO Automation

- Keyword research automation
- Technical SEO auditing
- Content generation
- Competitor analysis
- SEO monitoring
- Reporting

## React Components

The website is built with React and includes the following components:

### Layout Components
- **Layout**: Main layout wrapper for consistent page structure
- **Header**: Site header with logo and contact information
- **Navigation**: Responsive navigation menu with mobile support
- **Footer**: Site footer with links and contact information

### Page Components
- **HomePage**: Landing page with course information and features
- **NotFoundPage**: Custom 404 page with helpful navigation

### Blog Components
- **BlogPost**: Main component for displaying blog posts
- **BlogList**: Component for displaying a list of blog posts
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

### Running the Website

```
npm start
```

This will start the development server at http://localhost:3000

### Building for Production

```
npm run build
```

This will create an optimized production build in the `build` folder.

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
