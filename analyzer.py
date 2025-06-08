import sys

def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        char_count_no_spaces = len(text.replace(" ", ""))
        sentences = [s for s in text.split('.') if s.strip()]
        sentence_count = len(sentences)
        
        return {
            "word_count": word_count,
            "char_count": char_count,
            "char_count_no_spaces": char_count_no_spaces,
            "sentence_count": sentence_count
        }
    except FileNotFoundError:
        return {"error": "File not found"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 analyzer.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    result = analyze_text(file_path)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Word Count: {result['word_count']}")
        print(f"Character Count (with spaces): {result['char_count']}")
        print(f"Character Count (no spaces): {result['char_count_no_spaces']}")
        print(f"Sentence Count: {result['sentence_count']}")
