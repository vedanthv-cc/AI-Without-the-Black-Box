import math
from collections import Counter


corpus = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat and the dog are friends",
]


# --- from step 1: cosine similarity ---

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def magnitude(a):
    return math.sqrt(sum(x ** 2 for x in a))

def cosine_similarity(a, b):
    dp = dot_product(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dp / (mag_a * mag_b)


# --- from step 2: TF-IDF vectorization ---

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

def to_dense_vector(tfidf_scores, vocabulary):
    return [tfidf_scores.get(word, 0.0) for word in vocabulary]


# --- step 3: vectorize query using corpus vocabulary + IDF ---

def vectorize(text, idf_scores, vocabulary):
    tf = term_frequency(text)
    scores = {word: round(tf_score * idf_scores.get(word, 0), 4) for word, tf_score in tf.items()}
    return to_dense_vector(scores, vocabulary)


# --- build corpus vectors (done once) ---

idf_scores = inverse_document_frequency(corpus)
vocabulary = sorted(idf_scores.keys())
doc_vectors = [vectorize(doc, idf_scores, vocabulary) for doc in corpus]


# --- search ---

def search(query, corpus, doc_vectors, idf_scores, vocabulary):
    query_vector = vectorize(query, idf_scores, vocabulary)

    results = []
    for i, doc_vec in enumerate(doc_vectors):
        score = cosine_similarity(query_vector, doc_vec)
        results.append((score, i, corpus[i]))

    results.sort(reverse=True)
    return results


# --- run it ---

query = "cat and dog"

print(f"Query: '{query}'\n")
for score, i, doc in search(query, corpus, doc_vectors, idf_scores, vocabulary):
    print(f"  [{score:.4f}]  Doc {i+1}: {doc}")
