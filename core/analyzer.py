from core.llm_engine import query_llm
from core.classifier import classify_vulnerability
from core.scorer import calculate_score

def analyze_code(code: str, filename: str):

    prompt = f"""
You are a cybersecurity expert.

Analyze the following code and identify vulnerabilities.

Include severity level (Critical/High/Medium/Low),
explanation, and fix.

Code:
{code}
"""

    response = query_llm(prompt)

    vulnerability_type = classify_vulnerability(response)

    severity, score = calculate_score(response)

    result = {

        "file": filename,

        "vulnerability_type": vulnerability_type,

        "severity": severity,

        "score": score,

        "analysis": response
    }

    return result
