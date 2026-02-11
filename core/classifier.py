def classify_vulnerability(text: str):

    text = text.lower()

    if "buffer overflow" in text:
        return "Buffer Overflow"

    elif "sql injection" in text:
        return "SQL Injection"

    elif "command injection" in text:
        return "Command Injection"

    elif "xss" in text:
        return "Cross-Site Scripting"

    elif "hardcoded" in text:
        return "Hardcoded Credentials"

    elif "file handling" in text:
        return "Insecure File Handling"

    else:
        return "Unknown"
