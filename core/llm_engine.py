import subprocess

MODEL_NAME = "dolphin-mistral:7b"

def query_llm(prompt: str) -> str:

    try:
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if result.returncode != 0:
            return f"Error: {result.stderr}"

        return result.stdout.strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"
