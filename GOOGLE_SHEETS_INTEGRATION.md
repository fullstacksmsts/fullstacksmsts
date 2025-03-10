# Google Sheets Integration for SEO Automation

This document explains how to set up and use the Google Sheets integration for the SEO automation system.

## Overview

The SEO automation system can now automatically upload generated reports to Google Sheets. This allows for:

- Easy sharing of reports with team members
- Online access to reports from any device
- Integration with other Google Workspace tools
- Version history and collaboration features

## Setup Instructions

### 1. Google Cloud Project Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API and Google Drive API

### 2. Service Account Creation

1. In your Google Cloud project, navigate to "IAM & Admin" > "Service Accounts"
2. Create a new service account with a descriptive name (e.g., "seo-automation")
3. Grant the service account the necessary roles (at minimum, "Editor" role)
4. Create and download a JSON key for the service account
5. Rename the downloaded file to `google-credentials.json` and place it in the root directory of the SEO automation project

### 3. Google Sheets Setup

1. Create a new Google Spreadsheet or use an existing one
2. Share the spreadsheet with the service account email address (found in the credentials JSON file under `client_email`)
3. Copy the spreadsheet ID from the URL (the long string between `/d/` and `/edit` in the URL)

### 4. Configuration

Update the `config.json` file with your Google Sheets settings:

```json
"reporting": {
    "report_type": "monthly",
    "metrics": [...],
    "email_recipients": [...],
    "google_sheets": {
        "enabled": true,
        "credentials_file": "google-credentials.json",
        "spreadsheet_id": "YOUR_SPREADSHEET_ID_HERE",
        "share_with": ["optional_email@example.com"]
    }
}
```

- `enabled`: Set to `true` to enable Google Sheets integration
- `credentials_file`: Path to your service account credentials JSON file
- `spreadsheet_id`: ID of your Google Spreadsheet
- `share_with`: Optional list of email addresses to share the reports with

## Usage

Once configured, the Google Sheets integration will automatically:

1. Create a new sheet in your spreadsheet for each generated report
2. Upload the report data to the new sheet
3. Share the report with specified email addresses (if any)

You can run the reporting process with:

```bash
python master_automation.py --process reporting
```

Or run the full automation process with:

```bash
python master_automation.py
```

## Troubleshooting

If you encounter issues with the Google Sheets integration:

1. Check that the service account has edit access to the spreadsheet
2. Verify that the spreadsheet ID in the configuration is correct
3. Ensure the credentials file is in the correct location and has the proper format
4. Check the logs for specific error messages

## Security Considerations

- Keep your service account credentials secure and never commit them to version control
- Use the principle of least privilege when assigning roles to the service account
- Regularly rotate service account keys for enhanced security
