def convert_to_sparql(query):
    # Dummy conversion (basic prototype)
    if "prime minister of india" in query.lower():
        return """
        SELECT ?pm WHERE {
          ?pm dbo:office dbr:Prime_Minister_of_India .
        }
        """
    return "SPARQL query not found"

if __name__ == "__main__":
    user_query = input("Enter your question: ")
    sparql = convert_to_sparql(user_query)
    print("\nGenerated SPARQL Query:")
    print(sparql)
