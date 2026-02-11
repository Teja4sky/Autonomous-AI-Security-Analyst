def calculate_score(text: str):

    text = text.lower()

    if "critical" in text:
        return ("Critical", 9.0)

    elif "high" in text:
        return ("High", 7.5)

    elif "medium" in text:
        return ("Medium", 5.0)

    elif "low" in text:
        return ("Low", 3.0)

    else:
        return ("Unknown", 0.0)
