"""Session01: String preprocessing and tokenization."""

import re


def clean_text(text: str) -> str:
    """Lowercase, remove punctuation and compress whitespace."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str):
    """Split cleaned text into words."""
    return clean_text(text).split()


if __name__ == "__main__":
    sample = (
        "Hello, world! This is a sample sentence. "
        "We are learning NLP with Python and NLTK."
    )

    cleaned = clean_text(sample)
    words = tokenize(sample)

    print("Original:")
    print(sample)
    print("\nCleaned:")
    print(cleaned)
    print("\nTokenized words:")
    print(words)
    print(f"\nWord count: {len(words)}")
