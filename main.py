import argparse
from core.file_scanner import scan_directory
from core.analyzer import analyze_code
from core.report_writer import save_report

def read_file(path):

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--scan", help="Scan directory")
    parser.add_argument("--file", help="Scan single file")

    args = parser.parse_args()

    results = []

    if args.scan:

        files = scan_directory(args.scan)

        for file in files:

            print(f"Analyzing {file}")

            code = read_file(file)

            results.append(analyze_code(code, file))

    elif args.file:

        code = read_file(args.file)

        results.append(analyze_code(code, args.file))

    else:

        print("Use --scan or --file")

        return

    txt, json = save_report(results)

    print("\nReport saved:")
    print(txt)
    print(json)

if __name__ == "__main__":
    main()
