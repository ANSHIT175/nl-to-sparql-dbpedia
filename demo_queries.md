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


