def analyze_text(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Count words
        words = text.split()
        word_count = len(words)
        
        # Count characters
        char_count = len(text)
        char_count_no_spaces = len(text.replace(" ", ""))
        
        # Count sentences (basic: split by '.', '!', or '?')
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
    result = analyze_text("sample.txt")
    print(result)
