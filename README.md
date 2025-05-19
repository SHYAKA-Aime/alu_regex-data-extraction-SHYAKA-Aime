# Regex Data Extraction

This Python project extracts **emails, URLs, phone numbers, credit cards, time formats, HTML tags, hashtags, and currency amounts** from given Text using regular expressions.

---

## Features

- Accurate regex extraction
- Edge case handling (formats, spacing, punctuation)

---

### How to Run the Project

```bash
git clone https://github.com/SHYAKA-Aime/alu_regex-data-extraction-SHYAKA-Aime.git
cd alu_regex-data-extraction-SHYAKA-Aime
python main.py

```

Regex Patterns

Email Addresses

Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
Matches: user@example.com, firstname.lastname@company.co.uk

URLs

Pattern: `https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:/[^\s]*)?`
Matches: https://www.example.com, https://subdomain.example.org/page

Phone Numbers

Pattern: `(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-\.]\d{3}[-\.]\d{4})`
Matches: (123) 456-7890, 123-456-7890, 123.456.7890

Credit Card Numbers

Pattern: `\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}`
Matches: 1234 5678 9012 3456, 1234-5678-9012-3456

Time Formats

Pattern: `(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9])`
Matches: 14:30 (24-hour format), 2:30 PM (12-hour format)

HTML Tags

Pattern: `<[^>]+>`
Matches: <p>, <div class="example">, <img src="image.jpg" alt="description">

Hashtags

Pattern: `#[a-zA-Z0-9_]+`
Matches: #example, #ThisIsAHashtag

Currency Amounts

Pattern: `\$\d{1,3}(?:,\d{3})*\.\d{2}`
Matches: $19.99, $1,234.56

Testing

- The script includes sample text that tests all patterns. When run, it will extract and display all matches from the sample text.
