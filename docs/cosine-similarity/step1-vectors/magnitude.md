# Magnitude (Vector Length)

## Simple Intuition

Magnitude is just the **length of a vector** — how "big" it is, regardless of direction.

If a vector is an arrow, the dot product tells you how much two arrows agree in direction. The magnitude tells you how long each arrow is.

---

## The Formula

For a vector `A = [a1, a2, a3, ...]`:

```
|A| = sqrt(a1² + a2² + a3² + ...)
```

Square each element, add them all up, take the square root.

This is just the **Pythagorean theorem extended to N dimensions**.

---

## Worked Example

```
A = [1, 2, 3]

|A| = sqrt(1² + 2² + 3²)
    = sqrt(1 + 4 + 9)
    = sqrt(14)
    ≈ 3.74
```

In `scratch.py`, the `magnitude()` function does exactly this:
```
sum(x ** 2 for x in a)  →  adds up squares
math.sqrt(...)          →  takes the square root
```

---

## Why Magnitude Matters for Cosine Similarity

Two vectors can point in the same direction but have very different magnitudes:

```
A = [1, 2, 3]    |A| ≈ 3.74
D = [2, 4, 6]    |D| ≈ 7.48   (same direction, 2x longer)
```

If you only used the dot product to compare them, `D` would always score higher just because it's longer — not because it's more similar.

Dividing by both magnitudes in cosine similarity cancels this out:

```
cosine_similarity(A, D) = (A · D) / (|A| × |D|) = 1.0
```

The result is 1.0 — perfect similarity — because direction is all that matters.

---

## Where Magnitude Shows Up in AI

| Use Case | How |
|----------|-----|
| **Cosine similarity** | Dividing by magnitude normalizes vectors to direction-only |
| **Normalizing embeddings** | Dividing a vector by its own magnitude gives a unit vector (`|v| = 1`) |
| **L2 regularization** | Penalizes large weights by adding magnitude to the loss function |
| **Gradient norms** | Tracking `|gradient|` to detect exploding/vanishing gradients |

---

> Related: [dot-product.md](dot-product.md) — magnitude and dot product together are the two building blocks of cosine similarity. See [README.md](../README.md) for how they combine.
