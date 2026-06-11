# Step 3 — Search: Query vs Documents

## The Big Picture

Steps 1 and 2 gave us two tools:
- A way to measure similarity between two vectors (cosine similarity)
- A way to turn text into vectors (TF-IDF)

Step 3 combines them into a **search pipeline**:

```
Query (text)
    ↓  vectorize with same vocabulary + IDF from corpus
Query vector
    ↓  cosine similarity against every doc vector
Similarity scores
    ↓  sort descending
Ranked results
```

---

## The Pipeline

### 1. Build the corpus vectors (done once)

Compute IDF and vocabulary from your documents. Vectorize each document into a TF-IDF vector. These are stored and reused for every query.

```
corpus → IDF scores + vocabulary → doc vectors[]
```

### 2. Vectorize the query (done per query)

Take the query text and compute its TF-IDF vector — but using the **same vocabulary and IDF scores** from the corpus. Do not recompute IDF with the query included.

> This is the critical step. See [query-vectorization.md](query-vectorization.md) for why it must be this way.

```
query text → TF → multiply by corpus IDF → query vector
```

### 3. Score and rank

Compute cosine similarity between the query vector and each document vector. Sort by score descending.

```
for each doc vector:
    score = cosine_similarity(query_vector, doc_vector)

sort by score → ranked results
```

---

## Worked Example

```
Corpus:
  Doc 1: "the cat sat on the mat"
  Doc 2: "the dog sat on the log"
  Doc 3: "the cat and the dog are friends"

Query: "cat and dog"
```

After vectorizing with the corpus vocabulary and scoring:

```
[0.812]  Doc 3: "the cat and the dog are friends"
[0.391]  Doc 1: "the cat sat on the mat"
[0.391]  Doc 2: "the dog sat on the log"
```

Doc 3 scores highest because it contains both "cat" and "dog" — which are the two meaningful words in the query. Docs 1 and 2 each match only one.

---

## Code Walkthrough

See [scratch.py](scratch.py). Key things to observe when running it:

- `query_vector` is the same length as every doc vector — same vocabulary
- Words in the query that are not in the vocabulary get score `0.0` — they are ignored
- `"and"` in the query has a high IDF (rare in corpus) so it boosts Doc 3's score
- `"the"` in any query would contribute nothing — IDF zeroes it out

---

## What This Teaches

This is the core of how text search works at a basic level — before neural networks, before embeddings. Tools like **ElasticSearch** and **Solr** used TF-IDF ranking for years. Understanding this makes it much easier to reason about why modern embedding-based search (Step 4) is an improvement.
