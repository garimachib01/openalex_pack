"""Define test for search_works function."""
import os
import requests
from collections.abc import Iterable
import pandas as pd
import pytest
from oa_search_cite import search_works


def test_search_works():
    """Test search_works function."""
    # Call the function under test with a keyword
    result = search_works("reinforcement learning")

    # Assert the result is a DataFrame
    assert isinstance(result, pd.DataFrame)

    # Assert the DataFrame has the expected columns
    expected_columns = {"Title", "Citation Count", "ID", "Relevance Score"}
    assert set(result.columns) == expected_columns

    sorted_result = result.sort_values(by="Relevance Score", ascending=False)
    assert result.equals(sorted_result)

    # Assert the DataFrame has the correct number of rows
    if len(result) < 20:
        assert len(result) == len(sorted_result)
    else:
        assert len(result) == 20
