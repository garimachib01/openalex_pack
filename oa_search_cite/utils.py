"""Define utility functions for our package."""
import requests
from collections.abc import Iterable
import pandas as pd


def search_works(query):
    """Search works using OpenAlex API.

    Args:
        query (str or Iterable[str]):
        The query string or a list of terms in the query.

    Returns:
        pd.DataFrame: DataFrame containing search results with columns:
            - "Title": Title of the work.
            - "Citation Count": Number of citations for the work.
            - "Open Alex ID": Unique identifier of the work in OpenAlex.
            - "Relevance Score": Relevance score of the work.
    """
    if isinstance(query, str):
        query = "+".join(query.split())
    elif isinstance(query, Iterable):
        query = "+".join(query)

    endpoint = f"https://api.openalex.org/works?search={query}"
    response = requests.get(endpoint)
    results = response.json()

    # Extract relevant information from the results
    work_data = []
    for result in results.get("results", []):
        title = result["title"]
        citation_count = result["cited_by_count"]
        open_alex_id = result["id"]
        relevance_score = result["relevance_score"]

        work_data.append(
            {
                "Title": title,
                "Citation Count": citation_count,
                "ID": open_alex_id,
                "Relevance Score": relevance_score,
            }
        )

    # Create a DataFrame from the extracted information
    df = pd.DataFrame(work_data)

    # Sort DataFrame based on relevance score in descending order
    df_sorted = df.sort_values(by="Relevance Score", ascending=False)

    # Output top 20 works
    top_20_works = df_sorted.head(20)
    return top_20_works


def get_citation_trends(open_alex_id):
    """Get citation trends for a work using OpenAlex API.

    Args:
        open_alex_id (str): The Open Alex ID of the work.

    Returns:
        tuple: A tuple with the title of the work and its citation trends.
    """
    endpoint = f"https://api.openalex.org/works/{open_alex_id}"
    response = requests.get(endpoint)
    results = response.json()

    # Extract citation trends data
    citation_trends = results["counts_by_year"]
    title = results["title"]
    return title, citation_trends
