
# PhishGuard

PhishGuard is a full-stack phishing risk analysis web application built with Python, Flask, and SQLite. It helps users identify potentially suspicious emails by analyzing sender domains, message content, and URLs.

The application generates a risk score, explains detected indicators, and stores scan results for later review.

## Features

- **Email Analysis:** Analyze sender addresses, subjects, and email messages.
- **Phishing Detection:** Identify suspicious phrases, insecure HTTP links, and URLs containing IP addresses.
- **Domain Impersonation Detection:** Use Levenshtein distance to identify lookalike sender domains.
- **Risk Scoring:** Classify emails as Low, Medium, or High Risk using weighted detection rules.
- **Explainable Results:** Display the indicators that contributed to each risk score.
- **Scan History:** Store and review previous analyses using SQLite.
- **Web Interface:** Navigate between the email analyzer and scan history pages.

## Technologies Used

- Python
- Flask
- SQLite / SQL
- HTML
- CSS
- Git and GitHub

## How It Works

1. The user enters an email's sender address, subject, and message.
2. Flask sends the information to the Python detection engine.
3. The engine checks for suspicious language, links, and lookalike domains.
4. PhishGuard calculates a risk score from 0 to 100.
5. The application displays the findings and saves the scan results in SQLite.

## Installation

Clone the repository:

```bash
git clone https://github.com/AnthonyLoera10/PhishGuard-.git
cd PhishGuard-
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Flask:

```bash
python -m pip install flask
```

Run the application:

```bash
python app.py
```

Open http://127.0.0.1:5001 in your browser.

## Project Structure

```text
PhishGuard/
├── app.py
├── detector.py
├── database.py
├── templates/
│   ├── index.html
│   └── history.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

## Current Limitations

PhishGuard is an ongoing educational project. Its detection engine uses heuristic rules and a limited collection of trusted domains.

Risk scores are indicators of potentially suspicious characteristics, not verified probabilities of phishing. A low score does not guarantee an email is safe.

The application does not currently verify email authentication headers or provide production-grade phishing protection.

## Future Improvements

- Expand URL and domain analysis.
- Add automated detection tests and evaluate false positives.
- Improve scan history and analytics.
- Add options to manage or delete stored scans.
- Improve the responsive user interface.

## Project Status

In active development — july 2026 to Present.
