import sys

def read_file_to_set(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        print(f"Error: File not found - {filename}")
        return set()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return set()

def find_common_words(files):
    sets = [read_file_to_set(file) for file in files]

    if not sets:
        print("No valid files provided.")
        sys.exit(1)

    common_words = set.intersection(*sets) if sets else set()

    return common_words

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python common.py file1.txt file2.txt [file3.txt ...]")
        sys.exit(1)

    files = sys.argv[1:]
    common_words = find_common_words(files)

    if common_words:
        print("\n".join(sorted(common_words)))
    else:
        print("No common words found.")
