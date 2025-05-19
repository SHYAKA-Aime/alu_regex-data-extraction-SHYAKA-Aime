#!/usr/bin/env python3
import re

# Regex patterns for the data types

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:/[^\s]*)?'
phone_pattern = r'(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-\.]\d{3}[-\.]\d{4})'
credit_card_pattern = r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'
time_pattern = r'(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9])'
html_pattern = r'<[^>]+>'
hashtag_pattern = r'#[a-zA-Z0-9_]+'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}'


# Function to extract data from the given text using Regex patterns.

def extract_data(text):

    results = {
        'emails': re.findall(email_pattern, text),
        'urls': re.findall(url_pattern, text),
        'phone_numbers': re.findall(phone_pattern, text),
        'credit_cards': re.findall(credit_card_pattern, text),
        'times': re.findall(time_pattern, text),
        'html_tags': re.findall(html_pattern, text),
        'hashtags': re.findall(hashtag_pattern, text),
        'currency_amounts': re.findall(currency_pattern, text)
    }
    return results


# Run the Function

sample_text = """
Visit our website https://www.example.com or https://subdomain.example.org/page
Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890
Payment with card 1234 5678 9012 3456 or 1234-5678-9012-3456
Meeting at 14:30 or 2:30 PM
Special offer for $19.99 or premium at $1,234.56
<div class="container"><p>This is HTML content</p></div>
Contact us at user@example.com or firstname.lastname@company.co.uk
Follow us with #example and #ThisIsAHashtag
"""

results = extract_data(sample_text)

# Print extracted data
print("Extracted patterns from sample text: \n")
for data_type, items in results.items():
    print(f"\n{data_type.replace('_', ' ').title()}:")
    for item in items:
        print(f"  - {item}")