"""Session 1: Python foundations for text analysis."""


def count_text_features(text: str):
    """Return basic text metrics."""
    words = text.split()
    sentences = len([s for s in text.split('.') if s.strip()])
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": sentences,
        "lowercase": text.lower(),
        "stripped": text.strip(),
    }


if __name__ == "__main__":
    sample = input("Enter a paragraph: ")
    stats = count_text_features(sample)

    print(f"Characters: {stats['characters']}")
    print(f"Words: {stats['words']}")
    print(f"Sentences: {stats['sentences']}")
    print(f"Lowercase: {stats['lowercase']}")
    print(f"Trimmed: {stats['stripped']}")
