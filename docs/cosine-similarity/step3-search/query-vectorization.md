# Query Vectorization

## The Key Insight

When you vectorize a query, you **must** use the same vocabulary and IDF scores that were built from the corpus.

This is not obvious — here is why it has to work this way.

---

## Why the Same Vocabulary

The vocabulary defines the shape of every vector. If the corpus vocabulary has 10 words, every document vector has 10 positions — one per word.

For cosine similarity to work, the query vector must have the same 10 positions in the same order. If you built a new vocabulary from the query, positions would mean different things and the math would be nonsense.

```
Corpus vocabulary: ["and", "are", "cat", "dog", "friends", "log", "mat", "on", "sat", "the"]
                      [0]   [1]    [2]    [3]     [4]       [5]   [6]   [7]   [8]   [9]

Doc 1 vector:      [0.0,  0.0,  0.068,  0.0,   0.0,     0.0,  0.183, 0.068, 0.068, 0.0]
Query "cat":       [0.0,  0.0,  0.405,  0.0,   0.0,     0.0,  0.0,   0.0,   0.0,   0.0]
                                 ↑
                    same position, same meaning — now cosine similarity makes sense
```

---

## Why the Same IDF

IDF measures how rare a word is across the corpus. It was computed from the documents — it is a property of the corpus, not the query.

If you recomputed IDF with the query included, every query would change the meaning of the IDF scores and make all previous results inconsistent.

```
Corpus IDF["cat"] = log(3/2) ≈ 0.405   ← fixed, based on 3 documents
```

When vectorizing the query, you multiply query TF by this pre-computed IDF. You are asking: "how much does 'cat' matter, given what we know about this corpus?"

---

## What Happens to Unknown Words

If the query contains a word not in the vocabulary, it simply contributes nothing — `idf.get(word, 0)` returns 0.

```
Query: "elephant cat"
"elephant" → not in vocabulary → TF-IDF = 0.0 → ignored
"cat"       → in vocabulary   → TF-IDF = 0.405 → contributes
```

This is a known limitation of TF-IDF. If a user searches for a word that never appeared in any document, the query cannot find it. Embedding-based search (next step) solves this by using semantic meaning instead of exact word matches.

---

## TF for the Query

The only thing computed fresh for each query is the **term frequency** — how often each word appears in the query itself.

```
Query: "cat and cat"
TF("cat") = 2/3 ≈ 0.667
TF("and") = 1/3 ≈ 0.333

TF-IDF("cat") = 0.667 × IDF["cat"]
TF-IDF("and") = 0.333 × IDF["and"]
```

Repeating a word in the query boosts its weight — which is the expected behavior.

> Related: [README.md](README.md) for the full search pipeline
