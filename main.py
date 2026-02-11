from analyzer import analyze_code

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():

    file_path = "test_code.c"

    code = read_file(file_path)

    print("Analyzing code...\n")

    result = analyze_code(code)

    print("Security Report:\n")
    print(result)

if __name__ == "__main__":
    main()
