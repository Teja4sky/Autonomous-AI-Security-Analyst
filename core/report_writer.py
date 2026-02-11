import os
from datetime import datetime

REPORT_DIR = "reports"

def save_report(results: list):

    os.makedirs(REPORT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report_path = os.path.join(
        REPORT_DIR,
        f"security_report_{timestamp}.txt"
    )

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("AUTONOMOUS AI SECURITY ANALYST REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Generated on: {datetime.now()}\n")
        file.write(f"Total files analyzed: {len(results)}\n\n")

        for index, result in enumerate(results, start=1):

            file.write("=" * 60 + "\n")
            file.write(f"FILE {index}: {result['file']}\n")
            file.write("=" * 60 + "\n\n")

            file.write(result["analysis"])
            file.write("\n\n")

        file.write("=" * 60 + "\n")
        file.write("END OF REPORT\n")
        file.write("=" * 60 + "\n")

    return report_path
