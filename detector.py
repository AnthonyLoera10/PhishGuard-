
import re


def levenshtein_distance(s1, s2):
    previous_row = list(range(len(s2) + 1))

    for i, char1 in enumerate(s1, 1):
        current_row = [i]

        for j, char2 in enumerate(s2, 1):
            insert = current_row[j - 1] + 1
            delete = previous_row[j] + 1
            replace = previous_row[j - 1] + (char1 != char2)

            current_row.append(min(insert, delete, replace))

        previous_row = current_row

    return previous_row[-1]


SUSPICIOUS_PHRASES = [
    "verify your account",
    "account suspended",
    "urgent action",
    "click here",
    "confirm your identity",
    "password expired",
    "immediate action",
    "unusual activity"
]


def analyze_email(sender, subject, message):
    score = 0
    findings = []

    text = (subject + " " + message).lower()

   
   
    # Detect lookalike sender domains
    trusted_domains = [
        "paypal.com",
        "amazon.com",
        "microsoft.com",
        "google.com"
    ]

    sender_domain = sender.strip().lower().split("@")[-1]

    for official_domain in trusted_domains:
        if sender_domain == official_domain:
            continue

        # Compare domains using similarity
        similarity = sum(
            a == b
            for a, b in zip(sender_domain, official_domain)
        )

        similarity_score = similarity / max(
            len(sender_domain), len(official_domain)
        )

        
        # Compare domains using Levenshtein distance
        distance = levenshtein_distance(
            sender_domain, official_domain
        )

        if distance == 1:
            score += 30
            findings.append(
                f"Possible domain impersonation: {sender_domain} "
                f"resembles {official_domain}"
            )
            break


    

    # Check for suspicious phrases
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in text:
            score += 15
            findings.append(
                f"Suspicious phrase detected: '{phrase}'"
            )

    # Extract links from the email
    urls = re.findall(r'https?://[^\s<>"]+', message)

    # Check for insecure HTTP links
    for url in urls:
        if url.lower().startswith("http://"):
            score += 20
            findings.append(
                "Potentially insecure HTTP link detected"
            )

    # Check for IP addresses in links
    for url in urls:
        if re.search(r'https?://\d{1,3}(?:\.\d{1,3}){3}(?:[:/]|$)', url):
            score += 25
            findings.append(
                "Link uses an IP address instead of a domain"
            )

    score = min(score, 100)

    if score >= 60:
        risk = "High Risk"
    elif score >= 30:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return {
        "score": score,
        "risk": risk,
        "findings": findings
    }
