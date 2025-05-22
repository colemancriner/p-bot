# P-Bot

A bot for monitoring product availability on e-commerce websites and sending notifications when items become available.

## Features

-   Monitors product availability on websites
-   Uses BeautifulSoup for HTML parsing
-   Implements random delays and user agent rotation to avoid detection
-   Sends email notifications when products become available

## Limitations

-   The current BeautifulSoup implementation does not work on dynamic websites that load content via JavaScript
-   Future versions will implement Selenium or Playwright for full browser automation

## Setup

1. Ensure you have the required dependencies installed:

    ```
    pip install beautifulsoup4 requests ezgmail
    ```

2. Configure the credentials.json file for Gmail API access
