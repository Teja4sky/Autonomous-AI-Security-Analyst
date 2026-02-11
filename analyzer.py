from llm_engine import query_llm

def analyze_code(code):

    prompt = f"""
You are an expert cybersecurity analyst.

Analyze the following code for security vulnerabilities.

Provide output in this format:

Vulnerabilities Found:
Severity:
Explanation:
Fix:
Secure Code Example:

Code:
{code}
"""

    response = query_llm(prompt)
    return response
