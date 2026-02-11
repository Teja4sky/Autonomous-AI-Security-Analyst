import subprocess

def query_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "dolphin-mistral:7b"],
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
