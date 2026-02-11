from core.llm_engine import query_llm

def analyze_code(code: str, filename: str) -> dict:

    prompt = f"""
You are an expert cybersecurity analyst.

Analyze the following source code file and identify all security vulnerabilities.

Provide structured output:

Vulnerabilities Found:
Severity:
Explanation:
Recommended Fix:

File Name: {filename}

Code:
{code}
"""

    response = query_llm(prompt)

    result = {
        "file": filename,
        "analysis": response
    }

    return result
