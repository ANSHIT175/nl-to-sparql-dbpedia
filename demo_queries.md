# 🔍 Demo Queries

This file contains example natural language queries and their corresponding SPARQL queries.

---

### Query 1
**Input:** Who is the Prime Minister of India?

**SPARQL:**
```sparql
SELECT ?pm WHERE {
  ?pm dbo:office dbr:Prime_Minister_of_India .
}

Query 2

Input: What is the capital of India?

SPARQL:

SELECT ?capital WHERE {
  dbr:India dbo:capital ?capital .
}
Query 3

Input: Who is the President of India?

SPARQL:

SELECT ?president WHERE {
  ?president dbo:office dbr:President_of_India .
}
