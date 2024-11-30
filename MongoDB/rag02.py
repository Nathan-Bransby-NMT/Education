
"""
Retrieving the Data

This code implements the retriever component of our RAG system, using Atlas Vector Search. You can also view or fork the code from the Curriculum GitHub repository.

Prerequisites

Atlas Cluster Connection String
OpenAI API Key
Data loaded into Atlas
"""

'''
Create the following vector search index, named vector_index, on the chunked_data collection in your Atlas Cluster

{
  "fields": [
    {
      "numDimensions": 1536,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    },
    {
      "path": "hasCode",
      "type": "filter"
    }
  ]
}
'''

dbName = "book_mongodb_chunks"
collectionName = "chunked_data"
index = "vector_index"

vectorStore = MongoDBAtlasVectorSearch.from_connection_string(
    key_param.MONGODB_URI,
    dbName + "." + collectionName,
    OpenAIEmbeddings(disallowed_special=(), openai_api_key=key_param.LLM_API_KEY),
    index_name=index,
)

def query_data(query):
    retriever = vectorStore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3
        },
    )

    results = retriever.invoke(query)
    print(results)