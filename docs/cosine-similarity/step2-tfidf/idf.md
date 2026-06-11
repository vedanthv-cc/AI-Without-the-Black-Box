# Inverse Document Frequency (IDF)

## Simple Intuition

TF alone has a problem — common words like "the", "is", "a" appear frequently in every document. They'd score high on TF but carry no actual meaning.

IDF answers: **how rare or unique is this word across all documents?**

- A word that appears in every document → not useful → gets a **low** IDF score
- A word that appears in only a few documents → distinctive → gets a **high** IDF score

---

## The Formula

```
IDF(word) = log( N / df )
```

Where:
- `N` = total number of documents in the corpus
- `df` = number of documents that contain the word
- `log` dampens the scale so rare words don't dominate completely

---

## Worked Example

```
Corpus (3 documents):
  Doc 1: "the cat sat on the mat"
  Doc 2: "the dog sat on the log"
  Doc 3: "the cat and the dog are friends"

N = 3
```

| Word | Appears in (df) | IDF = log(3/df) |
|------|----------------|-----------------|
| the  | 3 docs         | log(3/3) = log(1) = 0.0 |
| cat  | 2 docs         | log(3/2) ≈ 0.405 |
| sat  | 2 docs         | log(3/2) ≈ 0.405 |
| dog  | 2 docs         | log(3/2) ≈ 0.405 |
| friends | 1 doc       | log(3/1) ≈ 1.099 |
| mat  | 1 doc          | log(3/1) ≈ 1.099 |

Key observation: **"the" gets IDF = 0** — it appears in every document so it gets completely zeroed out. "friends" and "mat" are unique to one document so they score highest.

---

## Why log()?

Without log, a word in 1 out of 1000 documents would get IDF = 1000 — way too dominant.
Log compresses the scale:

```
log(1000/1) ≈ 6.9   instead of 1000
log(1000/10) ≈ 4.6  instead of 100
log(1000/100) ≈ 2.3 instead of 10
```

Still ranks rare words higher, but keeps the numbers reasonable.

---

## Where IDF Shows Up in AI

| Use Case | How |
|----------|-----|
| **TF-IDF** | IDF is the other half — penalizes common words across the corpus |
| **Search engines** | IDF is part of BM25, a common ranking algorithm |
| **Keyword extraction** | High IDF words are good candidates for document keywords |

> Related: [tf.md](tf.md) and [tfidf.md](tfidf.md)
