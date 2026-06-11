# Dot Product

## Simple Intuition

Think of two vectors as lists of numbers representing something — maybe how much a movie has "action" and "romance":

```
Movie A = [8, 2]   (lots of action, little romance)
Movie B = [7, 3]   (similar)
Movie C = [1, 9]   (very different — mostly romance)
```

The dot product tells you **how much two vectors "agree"** — how aligned they are in the same direction.

- High dot product → pointing in similar direction → similar things
- Low / negative → pointing away → different things

---

## The Formula

Given two vectors **A** and **B** of the same length:

```
A · B = (A[0] × B[0]) + (A[1] × B[1]) + ... + (A[n] × B[n])
```

Multiply each pair of corresponding elements, then add them all up. That's it.

---

## Worked Example

```
A = [1, 2, 3]
B = [4, 5, 6]

A · B = (1×4) + (2×5) + (3×6)
      = 4 + 10 + 18
      = 32
```

Now try with a very different vector:

```
A = [1, 2, 3]
C = [3, 2, 1]

A · C = (1×3) + (2×2) + (3×1)
      = 3 + 4 + 3
      = 10
```

`A · B = 32` vs `A · C = 10` — B is more "aligned" with A than C is.

---

## Why the Raw Dot Product Isn't Enough

The dot product is affected by **magnitude** (the length of the vectors).

```
A = [1, 2, 3]   →  shorter vector
D = [10, 20, 30] →  same direction, but 10x longer

A · D = 10 + 40 + 90 = 140   ← large, but only because D is big
```

A and D point in exactly the same direction but the dot product is huge. This is a problem when comparing things like word embeddings or document vectors — a longer document shouldn't automatically be more "similar."

**This is exactly why cosine similarity exists** — it divides the dot product by the magnitudes to normalize it. See [README.md](../README.md).

---

## Where Dot Products Show Up in AI

| Use Case | How |
|----------|-----|
| **Cosine similarity** | Dot product ÷ magnitudes = direction-only comparison |
| **Neural network layers** | Every dense/linear layer computes `W · x + b` |
| **Attention (Transformers)** | Query · Key dot product decides what to "pay attention to" |
| **Recommendation systems** | User vector · Item vector → relevance score |

The dot product is one of the most fundamental operations in ML. Understanding it makes attention mechanisms and embeddings much easier to reason about.
