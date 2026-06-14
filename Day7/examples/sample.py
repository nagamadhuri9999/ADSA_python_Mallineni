def main():
    print("This is a sample Python script accompanying sample.md")
    
    # Example of reading sample.md
    try:
        with open("sample.md", "r") as f:
            content = f.read()
            if not content.strip():
                print("sample.md is currently empty.")
            else:
                print("Contents of sample.md:")
                print(content)
    except FileNotFoundError:
        print("sample.md not found.")

if __name__ == "__main__":
    main()
