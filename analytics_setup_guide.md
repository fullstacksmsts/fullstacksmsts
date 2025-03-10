# Analytics Setup Guide for fullstacksmsts.co.uk

This guide provides instructions for setting up analytics tracking for the fullstacksmsts.co.uk SEO automation system. Proper analytics setup is essential for measuring the performance of SEO efforts and making data-driven decisions.

## Google Analytics 4 Setup

### 1. Create a Google Analytics 4 Property

1. Sign in to [Google Analytics](https://analytics.google.com/)
2. Click "Admin" in the bottom left corner
3. In the Account column, select "Create Account" if you don't have one, or select an existing account
4. In the Property column, click "Create Property"
5. Select "Web" as the platform
6. Enter "Full Stack SMSTS" as the website name
7. Enter "fullstacksmsts.co.uk" as the website URL
8. Select your industry category and reporting time zone
9. Click "Create"

### 2. Set Up Data Streams

1. In the Property column, click "Data Streams"
2. Click "Add Stream" and select "Web"
3. Enter "fullstacksmsts.co.uk" as the website URL
4. Enter "Full Stack SMSTS Website" as the stream name
5. Toggle on "Enhanced measurement" to track page views, scrolls, outbound clicks, site search, video engagement, and file downloads automatically
6. Click "Create Stream"
7. Note your Measurement ID (format: G-XXXXXXXX)

### 3. Install the Google Analytics Tag

#### Option 1: Google Tag Manager (Recommended)

1. Create a Google Tag Manager account if you don't have one
2. Create a new container for fullstacksmsts.co.uk
3. Add a new Google Analytics 4 Configuration tag
4. Enter your Measurement ID
5. Set the trigger to "All Pages"
6. Publish the container
7. Install the Google Tag Manager snippet in the `<head>` section of your website

#### Option 2: Direct Implementation

Add the following code to the `<head>` section of all pages on fullstacksmsts.co.uk:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXX');
</script>
```

Replace `G-XXXXXXXX` with your actual Measurement ID.

### 4. Set Up Conversion Tracking

#### Course Booking Conversions

1. In Google Analytics, go to "Admin" > "Events" > "Create Event"
2. Name the event "course_booking_completed"
3. Add the following conditions:
   - Event name equals "form_submit"
   - Page URL contains "/booking-confirmation"
4. Click "Create"
5. Go to "Admin" > "Conversions"
6. Click "New Conversion Event"
7. Select "course_booking_completed"
8. Click "Save"

#### Lead Form Submissions

1. In Google Analytics, go to "Admin" > "Events" > "Create Event"
2. Name the event "lead_form_submitted"
3. Add the following conditions:
   - Event name equals "form_submit"
   - Page URL contains "/contact-thank-you"
4. Click "Create"
5. Go to "Admin" > "Conversions"
6. Click "New Conversion Event"
7. Select "lead_form_submitted"
8. Click "Save"

#### Course Information Downloads

1. In Google Analytics, go to "Admin" > "Events" > "Create Event"
2. Name the event "course_info_downloaded"
3. Add the following conditions:
   - Event name equals "file_download"
   - File extension equals "pdf"
   - File name contains "smsts-course-information"
4. Click "Create"
5. Go to "Admin" > "Conversions"
6. Click "New Conversion Event"
7. Select "course_info_downloaded"
8. Click "Save"

## Google Search Console Setup

### 1. Add Property

1. Go to [Google Search Console](https://search.console.google.com/)
2. Click "Add Property"
3. Select "URL prefix" and enter "https://fullstacksmsts.co.uk/"
4. Verify ownership using one of the following methods:
   - HTML file upload
   - HTML tag
   - Google Analytics
   - Google Tag Manager
   - Domain name provider

### 2. Connect Google Analytics with Search Console

1. In Google Analytics, go to "Admin" > "Property Settings"
2. Scroll down to "Search Console Settings"
3. Click "Adjust Search Console"
4. Select your Search Console property
5. Click "Save"

## Custom Tracking Implementation

### 1. Track User Journey Stages

Add the following custom dimensions in Google Analytics:

1. Go to "Admin" > "Custom Definitions" > "Custom Dimensions"
2. Click "Create Custom Dimension"
3. Name it "User Journey Stage"
4. Set scope to "User"
5. Click "Save"

Implement the following code to track user journey stages:

```javascript
// Track awareness stage
if (window.location.pathname.includes('/what-is-smsts') || 
    window.location.pathname.includes('/guide-to-smsts')) {
  gtag('set', 'user_properties', {
    'journey_stage': 'awareness'
  });
}

// Track consideration stage
if (window.location.pathname.includes('/smsts-vs-') || 
    window.location.pathname.includes('/compare-smsts') ||
    window.location.pathname.includes('/smsts-course-options')) {
  gtag('set', 'user_properties', {
    'journey_stage': 'consideration'
  });
}

// Track conversion stage
if (window.location.pathname.includes('/book-smsts-course') || 
    window.location.pathname.includes('/smsts-course-booking')) {
  gtag('set', 'user_properties', {
    'journey_stage': 'conversion'
  });
}
```

### 2. Track Content Pillar Engagement

Add the following custom dimensions in Google Analytics:

1. Go to "Admin" > "Custom Definitions" > "Custom Dimensions"
2. Click "Create Custom Dimension"
3. Name it "Content Pillar"
4. Set scope to "Session"
5. Click "Save"

Implement the following code to track content pillar engagement:

```javascript
// Map URL patterns to content pillars
const contentPillarMapping = {
  '/understanding-citb-smsts-courses': 'Understanding CITB SMSTS Courses',
  '/smsts-course-delivery': 'Navigating SMSTS Course Delivery and Providers',
  '/smsts-course-content': 'SMSTS Course Content and Assessment',
  '/smsts-vs-other-certifications': 'SMSTS vs. Other Certifications',
  '/implementing-smsts-knowledge': 'Implementing SMSTS Knowledge on Site'
};

// Find matching content pillar for current page
for (const [urlPattern, pillarName] of Object.entries(contentPillarMapping)) {
  if (window.location.pathname.includes(urlPattern)) {
    gtag('set', 'content_pillar', pillarName);
    break;
  }
}
```

### 3. Track Location-Specific Pages

Add the following custom dimensions in Google Analytics:

1. Go to "Admin" > "Custom Definitions" > "Custom Dimensions"
2. Click "Create Custom Dimension"
3. Name it "Location"
4. Set scope to "Session"
5. Click "Save"

Implement the following code to track location-specific page views:

```javascript
// Extract location from URL for location-specific pages
const locationMatch = window.location.pathname.match(/smsts-course-([a-z-]+)/);
if (locationMatch && locationMatch[1]) {
  const location = locationMatch[1].replace('-', ' ');
  gtag('set', 'location', location);
}
```

## Google Tag Manager Advanced Setup

For more advanced tracking, consider implementing the following tags in Google Tag Manager:

### 1. Enhanced Ecommerce Tracking

1. Create a new tag in Google Tag Manager
2. Select "Google Analytics: GA4 Event"
3. Configure the tag with the following settings:
   - Event Name: "purchase"
   - Event Parameters:
     - currency: "GBP"
     - value: "{{Course Price}}"
     - items: "[{item_id: 'SMSTS-COURSE', item_name: 'SMSTS Course', price: 360}]"
4. Set the trigger to fire on the booking confirmation page

### 2. Scroll Depth Tracking

1. Create a new tag in Google Tag Manager
2. Select "Google Analytics: GA4 Event"
3. Configure the tag with the following settings:
   - Event Name: "scroll"
   - Event Parameters:
     - percent_scrolled: "{{Scroll Depth Threshold}}"
4. Create a scroll depth trigger that fires at 25%, 50%, 75%, and 100% scroll depths

### 3. Outbound Link Tracking

1. Create a new tag in Google Tag Manager
2. Select "Google Analytics: GA4 Event"
3. Configure the tag with the following settings:
   - Event Name: "click"
   - Event Parameters:
     - link_url: "{{Click URL}}"
     - link_text: "{{Click Text}}"
     - outbound: "true"
4. Create a trigger that fires on clicks of links where the Click URL does not contain "fullstacksmsts.co.uk"

## Data Studio Reporting

### 1. Create a Data Studio Report

1. Go to [Google Data Studio](https://datastudio.google.com/)
2. Click "Create" > "Report"
3. Select Google Analytics 4 as the data source
4. Select your GA4 property
5. Click "Add to Report"

### 2. Set Up SEO Performance Dashboard

Create the following report pages:

1. **Executive Summary**
   - Month-over-month organic traffic
   - Conversion metrics
   - Top landing pages
   - Traffic by device
   - Traffic by location

2. **Organic Traffic Analysis**
   - Organic traffic trends
   - Traffic by content pillar
   - Traffic by user journey stage
   - New vs. returning users
   - Engagement metrics (bounce rate, session duration, pages per session)

3. **Conversion Analysis**
   - Conversion rate by source
   - Conversion rate by content pillar
   - Conversion rate by device
   - Conversion funnel visualization
   - Goal completions by page

4. **Content Performance**
   - Top performing pages
   - Content engagement by pillar
   - Page load time analysis
   - Scroll depth analysis
   - Exit page analysis

5. **Location Performance**
   - Traffic by location page
   - Conversion rate by location
   - Engagement metrics by location
   - Map visualization of user locations

## Integration with SEO Automation System

### 1. API Access Setup

1. Create a service account in Google Cloud Platform
2. Grant the service account access to your Google Analytics property
3. Download the service account credentials JSON file
4. Store the credentials file securely and reference it in your `.env` file

### 2. Configure Analytics in the SEO Automation System

Update your `.env` file with the following variables:

```
GA_PROPERTY_ID=123456789
GA_CLIENT_EMAIL=your-service-account@your-project.iam.gserviceaccount.com
GA_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nYour Private Key Here\n-----END PRIVATE KEY-----\n
GSC_SITE_URL=https://fullstacksmsts.co.uk/
```

### 3. Implement Automated Reporting

Use the Google Analytics Data API to pull data for your automated reports. Example Python code:

```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest

def get_ga4_data(property_id, dimensions, metrics, date_range):
    """Get data from Google Analytics 4."""
    client = BetaAnalyticsDataClient.from_service_account_json(
        'path/to/service-account-credentials.json'
    )
    
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[{"name": d} for d in dimensions],
        metrics=[{"name": m} for m in metrics],
        date_ranges=[date_range]
    )
    
    response = client.run_report(request)
    return response
```

## Verification and Testing

### 1. Verify Tracking Implementation

1. Install the [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna) Chrome extension
2. Enable the debugger and navigate to your website
3. Check the console logs to ensure events are firing correctly
4. Verify that custom dimensions are being set properly

### 2. Test Conversion Tracking

1. Complete a test booking on the website
2. Verify that the conversion event appears in Google Analytics
3. Check that the conversion is attributed to the correct source/medium
4. Verify that the conversion value is recorded correctly

### 3. Validate Data in Reports

1. Wait 24-48 hours for data to process
2. Check your Google Analytics reports to ensure data is being collected
3. Verify that custom dimensions are populated
4. Check that conversions are being tracked correctly

## Maintenance and Updates

### 1. Regular Checks

Perform the following checks monthly:

1. Verify that tracking is still working correctly
2. Check for any tracking errors in the Google Analytics interface
3. Ensure all conversion events are still firing
4. Validate that data is flowing into reports correctly

### 2. Updates for New Content

When adding new content to the website:

1. Update content pillar mapping if necessary
2. Add new location pages to location tracking
3. Configure additional conversion events for new conversion points
4. Update Data Studio reports to include new content categories

### 3. Annual Analytics Audit

Perform a comprehensive analytics audit annually:

1. Review tracking implementation
2. Update tracking code to latest versions
3. Evaluate additional tracking opportunities
4. Refine conversion tracking based on business goals
5. Update reporting dashboards to reflect current KPIs
