"""Tests for cohens_d: Cohen's d for two independent groups."""

import pytest
from cohensd import cohens_d

@pytest.fixture
def stub_data():
    return None

def test_stub(stub_data):
    """Test that the stub function returns None."""
    assert cohens_d(stub_data) is None