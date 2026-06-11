## What is Cosine Similarity?

Imagine each document is an arrow (vector) in space. **Cosine similarity** measures the angle between two arrows - not their length, just their direction.

- **Score = 1.0** → Same direction → Very similar
- **Score = 0.0** → Perpendicular → No similarity
- **Score = -1.0** → Opposite direction → Completely opposite

The formula:

`cosine_similarity(A, B) = (A · B) / (|A| × |B|)`

Where `A · B` is the dot product and `|A|`, `|B|` are the magnitudes.

> **Prerequisites:** Read [dot-product.md](step1-vectors/dot-product.md) to understand `A · B`, and [magnitude.md](step1-vectors/magnitude.md) to understand `|A|` and `|B|` — then the formula above will make complete sense.

## Learning Path

| Step | What | Code | Docs |
|------|------|------|------|
| 1 | Implement cosine similarity from scratch | [scratch.py](step1-vectors/scratch.py) | [dot-product.md](step1-vectors/dot-product.md), [magnitude.md](step1-vectors/magnitude.md) |
| 2 | Convert text to vectors with TF-IDF | [scratch.py](step2-tfidf/scratch.py) | [tfidf.md](step2-tfidf/tfidf.md) → [tf.md](step2-tfidf/tf.md), [idf.md](step2-tfidf/idf.md) |
| 3 | Search — query vs all documents | [scratch.py](step3-search/scratch.py) | [README.md](step3-search/README.md), [query-vectorization.md](step3-search/query-vectorization.md) |