import os
import json
from datetime import datetime

REPORT_DIR = "reports"

def save_report(results):

    os.makedirs(REPORT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_path = os.path.join(REPORT_DIR, f"report_{timestamp}.txt")
    json_path = os.path.join(REPORT_DIR, f"report_{timestamp}.json")

    critical = high = medium = low = 0

    with open(txt_path, "w", encoding="utf-8") as f:

        f.write("AI SECURITY ANALYSIS REPORT\n\n")

        for result in results:

            f.write(f"File: {result['file']}\n")
            f.write(f"Type: {result['vulnerability_type']}\n")
            f.write(f"Severity: {result['severity']}\n")
            f.write(f"Score: {result['score']}\n")
            f.write("-" * 50 + "\n")

            if result["severity"] == "Critical":
                critical += 1
            elif result["severity"] == "High":
                high += 1
            elif result["severity"] == "Medium":
                medium += 1
            elif result["severity"] == "Low":
                low += 1

        f.write("\nSUMMARY\n")
        f.write(f"Critical: {critical}\n")
        f.write(f"High: {high}\n")
        f.write(f"Medium: {medium}\n")
        f.write(f"Low: {low}\n")

    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(results, jf, indent=4)

    return txt_path, json_path
