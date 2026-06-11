# TF-IDF (Term Frequency–Inverse Document Frequency)

## Simple Intuition

TF-IDF converts raw text into a **numeric vector** so you can do math on it — like computing cosine similarity between two documents.

It solves a specific problem: words that appear a lot in a document are important, BUT only if they are also rare across the whole corpus. Common words like "the" should not dominate.

```
TF-IDF(word, document) = TF × IDF
```

- High TF-IDF → word is frequent in this doc AND rare overall → very relevant
- Low TF-IDF  → word is common everywhere (like "the") → not meaningful

> **Prerequisites:** Read [tf.md](tf.md) and [idf.md](idf.md) first — TF-IDF is just multiplying the two together.

---

## The Formula

```
TF-IDF(word, doc) = TF(word, doc) × IDF(word)

TF(word, doc)  = count(word in doc) / total words in doc
IDF(word)      = log( N / df )
```

---

## Worked Example

```
Corpus:
  Doc 1: "the cat sat on the mat"
  Doc 2: "the dog sat on the log"
  Doc 3: "the cat and the dog are friends"
```

Computing TF-IDF for the word **"cat"** in **Doc 1**:

```
TF("cat", Doc1)  = 1/6 ≈ 0.167     (appears 1 time, 6 total words)
IDF("cat")       = log(3/2) ≈ 0.405 (appears in 2 of 3 docs)

TF-IDF = 0.167 × 0.405 ≈ 0.068
```

Now for **"the"** in **Doc 1**:

```
TF("the", Doc1)  = 2/6 ≈ 0.333
IDF("the")       = log(3/3) = 0.0   (appears in every doc → zeroed out)

TF-IDF = 0.333 × 0.0 = 0.0
```

"the" is wiped out completely. "cat" survives.

---

## From Words to Vectors

Once you compute TF-IDF scores for all words, you arrange them into a vector using a shared vocabulary:

```
Vocabulary (sorted): ["and", "are", "cat", "dog", "friends", "log", "mat", "on", "sat", "the"]

Doc 1 vector: [0.0, 0.0, 0.068, 0.0, 0.0, 0.0, 0.183, 0.068, 0.068, 0.0]
Doc 2 vector: [0.0, 0.0, 0.0, 0.068, 0.0, 0.183, 0.0, 0.068, 0.068, 0.0]
```

These vectors can now be fed directly into `cosine_similarity()` from `../step1-vectors/scratch.py`.

---

## Where TF-IDF Shows Up in AI

| Use Case | How |
|----------|-----|
| **Document search** | Query and documents both become TF-IDF vectors, cosine similarity ranks results |
| **Text classification** | TF-IDF vectors as features for ML classifiers |
| **Keyword extraction** | Top TF-IDF scoring words = document keywords |
| **Baseline NLP** | Still used as a fast, interpretable baseline before trying embeddings |

TF-IDF is the bridge between raw text and the vector math you already know. See [scratch.py](scratch.py) to implement it from scratch.
