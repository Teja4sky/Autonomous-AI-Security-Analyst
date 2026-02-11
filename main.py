from core.file_scanner import scan_directory
from core.analyzer import analyze_code
from core.report_writer import save_report


def read_file(file_path: str):

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""


def main():

    target_directory = "samples"

    print(f"\nScanning directory: {target_directory}")

    files = scan_directory(target_directory)

    if not files:
        print("No supported files found.")
        return

    print(f"Found {len(files)} files\n")

    results = []

    for file in files:

        print(f"Analyzing: {file}")

        code = read_file(file)

        if code.strip() == "":
            continue

        analysis = analyze_code(code, file)

        results.append(analysis)

    report_path = save_report(results)

    print("\nAnalysis Complete")
    print(f"Report saved at: {report_path}")


if __name__ == "__main__":
    main()
