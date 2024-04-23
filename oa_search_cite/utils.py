"""Define utility functions for our package."""
import requests
from collections.abc import Iterable
import pandas as pd


def search_works(query):
    
    if isinstance(query, str):
        query = '+'.join(query.split())

    # We assume it is an iterable of strings.
    elif isinstance(query, Iterable):
        query = '+'.join(query)
        
    endpoint = f'https://api.openalex.org/works?search={query}'
    response = requests.get(endpoint)
    results = response.json()
       # Extract relevant information from the results
    work_data = []
    for result in results.get("results", []):
        title = result["title"]
        citation_count = result['cited_by_count']
        open_alex_id = result['id']
        relevance_score = result['relevance_score']
        
        work_data.append({
            "Title": title,
            "Citation Count": citation_count,
            "Open Alex ID": open_alex_id,
            "Relevance Score": relevance_score
        })

    # Create a DataFrame from the extracted information
    df = pd.DataFrame(work_data)

    # Sort DataFrame based on relevance score in descending order
    df_sorted = df.sort_values(by="Relevance Score", ascending=False)

    if len(df_sorted) < 20:
        return df_sorted
    else:
        return df_sorted.head(20)


def get_citation_trends(open_alex_id):
    endpoint = f'https://api.openalex.org/works/{open_alex_id}'
    response = requests.get(endpoint)
    results = response.json()
    # Extract citation trends data
    citation_trends = results["counts_by_year"]
    title = results["title"]
    return title, citation_trends
