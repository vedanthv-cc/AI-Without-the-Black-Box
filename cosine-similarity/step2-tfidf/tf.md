# Term Frequency (TF)

## Simple Intuition

Term Frequency answers: **how important is this word to this document?**

The simplest proxy — if a word appears a lot in a document, it's probably important to that document.

```
Document: "the cat sat on the mat the cat"
"cat" appears 2 times out of 8 total words → it matters here
"the" appears 3 times out of 8 → but it's just a filler word (IDF will handle this)
```

---

## The Formula

```
TF(word, document) = count of word in document / total words in document
```

Dividing by total words **normalizes** for document length — a 1000-word document shouldn't automatically score higher than a 10-word one.

---

## Worked Example

```
Document: "the cat sat on the mat the cat"
Total words: 8

TF("cat")  = 2/8 = 0.25
TF("the")  = 3/8 = 0.375
TF("sat")  = 1/8 = 0.125
TF("mat")  = 1/8 = 0.125
TF("on")   = 1/8 = 0.125
```

Notice that "the" has the highest TF — but it carries no real meaning. That's the problem TF alone can't solve. See [idf.md](idf.md) for how IDF penalizes common words like this.

---

## Where TF Shows Up in AI

| Use Case | How |
|----------|-----|
| **TF-IDF** | TF is half of the score — tells you word importance within one document |
| **Bag of Words** | Simple word count vectors (TF without the division) |
| **Search engines** | TF contributes to document relevance ranking |

> Related: [idf.md](idf.md) and [tfidf.md](tfidf.md)
