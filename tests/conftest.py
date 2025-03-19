import pytest
from pathlib import Path

@pytest.fixture
def resources() -> Path:
    return Path(__file__).parent / "resources"
