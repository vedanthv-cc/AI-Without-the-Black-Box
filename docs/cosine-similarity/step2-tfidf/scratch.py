import math
from collections import Counter


corpus = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat and the dog are friends",
]


def tokenize(doc):
    return doc.lower().split()


def term_frequency(doc):
    tokens = tokenize(doc)
    counts = Counter(tokens)
    total = len(tokens)
    return {word: count / total for word, count in counts.items()}


def inverse_document_frequency(corpus):
    N = len(corpus)
    all_words = set(word for doc in corpus for word in tokenize(doc))
    idf = {}
    for word in all_words:
        df = sum(1 for doc in corpus if word in tokenize(doc))
        idf[word] = math.log(N / df)
    return idf


def tfidf(doc, idf):
    tf = term_frequency(doc)
    return {word: round(tf_score * idf.get(word, 0), 4) for word, tf_score in tf.items()}


def to_dense_vector(tfidf_scores, vocabulary):
    return [tfidf_scores.get(word, 0.0) for word in vocabulary]


# --- build vectors ---

idf_scores = inverse_document_frequency(corpus)
vocabulary = sorted(idf_scores.keys())

vectors = []
for doc in corpus:
    scores = tfidf(doc, idf_scores)
    vec = to_dense_vector(scores, vocabulary)
    vectors.append(vec)

# Inspect: vocabulary and what each vector looks like
print("Vocabulary:", vocabulary)
for i, vec in enumerate(vectors):
    print(f"Doc {i+1} vector: {vec}")

# Now copy cosine_similarity from step1.py and compare:
# cosine_similarity(vectors[0], vectors[1]) — doc1 vs doc2
# cosine_similarity(vectors[0], vectors[2]) — doc1 vs doc3
