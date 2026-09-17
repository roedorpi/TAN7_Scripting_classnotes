"""Session 02: Building corpora with lists, dictionaries and loops."""


corpus = {
    "doc1": "python is a useful language for text analysis and learning",
    "doc2": "nlp helps computers understand language and find themes in text",
    "doc3": "text statistics show word frequency and lexical diversity across documents",
}


def word_counts(text: str):
    """Return a dictionary of word frequencies for a text."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(doc_text: str, n: int = 5):
    """Return the most frequent words in a document."""
    counts = word_counts(doc_text)
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:n]


if __name__ == "__main__":
    for title, text in corpus.items():
        print(f"\n--- {title} ---")
        counts = word_counts(text)
        print(counts)
        print("Top words:", top_words(text))

    total_words = sum(len(text.split()) for text in corpus.values())
    print(f"\nTotal words across corpus: {total_words}")
