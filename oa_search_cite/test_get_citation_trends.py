"""Define test for get_citation_trends function."""
import os
import pytest
import requests
from collections.abc import Iterable
from oa_search_cite import get_citation_trends


def test_get_citation_trends():
    """Test get_citation_trends function."""
    # Define a valid OpenAlex ID to query
    open_alex_id = "https://openalex.org/W2741809807"

    # Call the function under test with the OpenAlex ID
    title, citation_trends = get_citation_trends(open_alex_id)

    # Assert that the title is retrieved successfully
    assert isinstance(title, str)
    assert title != ""  # Ensure title is not empty

    # Assert that the citation trends are retrieved successfully
    assert isinstance(citation_trends, list)
    # Ensure at least one count is returned
    assert len(citation_trends) > 0

    # Ensure all counts are integers
    for result in citation_trends:
        assert isinstance(result["cited_by_count"], int)
        assert result["cited_by_count"] >= 0
