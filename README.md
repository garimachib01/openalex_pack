[![First job](https://github.com/garimachib01/openalex_pack/actions/workflows/my-workflow.yaml/badge.svg)](https://github.com/garimachib01/openalex_pack/actions/workflows/my-workflow.yaml)

# Keyword search and Citation Trends using OpenAlex: oa_search_cite 

This package simplifies searching and filtering for relevant academic works from the OpenAlex database based on user-provided keywords. An additional feature allows for the retrieval of citation data over time for a given academic work.

## Functions Provided:

1. **Keyword search**: This function looks for keyword matches in titles, abstracts, and fulltext in the OpenAlex database. It returns a Pandas dataframe with the titles of the top 20 works associated with the keyword, along with other fields like OpenAlex ID, citation count, and relevance score. Entries are sorted by relevance score. If fewer than 20 works match the keyword, the complete list is returned.

2. **Citation trends for a given work**: This function provides the citation trends by year for a given work. Users input an OpenAlex ID, and the output includes the title of the work and a list of dictionaries, each representing a year and its corresponding citation count.

## Usage 
To use the Python package `oa_search_cite`, clone this git repository and install it via pip. 
- To use the keyword search function, import the `search_works` function from `oa_search_cite` and provide the keywords as an argument. The output is a Pandas dataframe with the relevant fields.
- To use the citation trends function, import the `get_citation_trends` function from `oa_search_cite` and provide the OpenAlex ID in the format https://openalex.org/[id]. The function outputs the title of the work and citation counts over time.
