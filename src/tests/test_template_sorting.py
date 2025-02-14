import sys
sys.path.append("C:\\Users\\mvvsg\\AppData\\Local\\Programs\\Python\\Python313")
import pytest
import jsonschema
from src.schemas.template_schema import TEMPLATE_SCHEMA

base_config = {
    "bubbleDimensions" : [5, 5],
    "pageDimensions": [800, 600],
    "preProcessors": [],
    "fieldBlocks" : {}
}

valid_alphabetical_desc_config = {
    **base_config,
    "outputColumns": {
        "sortType" : "alphabetical",
        "sortOrder" : "desc"
    }
}

valid_alphabetical_asc_config = {
    **base_config,
    "outputColumns": {
        "sortType" : "alphabetical",
        "sortOrder" : "asc"
    }
}

valid_alphanumeric_asc_config = {
    **base_config,
    "outputColumns": {
        "sortType" : "alphanumeric",
        "sortOrder" : "asc"
    }
}

valid_alphanumeric_desc_config = {
    **base_config,
    "outputColumns": {
        "sortType" : "alphanumeric",
        "sortOrder" : "desc"
    }
}

valid_custom_asc_config = {
    **base_config,
    "outputColumns": {
        "sortType" : "custom",
        "sortOrder" : "asc",
        "columns": ["Q2", "Q10", "Q1", "A20", "A1"]
    }
}

valid_custom_desc_config = {
    **base_config,
    "outputColumns": {
        "sortType" : "custom",
        "sortOrder" : "desc",
        "columns": ["Q2", "Q10", "Q1", "A20", "A1"]
    }
}

@pytest.mark.parametrize("config", [
    valid_alphabetical_asc_config,
    valid_alphabetical_desc_config,
    valid_alphanumeric_asc_config,
    valid_alphanumeric_desc_config,
    valid_custom_asc_config,
    valid_custom_desc_config
])

def test_valid_template_schema(config):
    try:
        jsonschema.validate(instance=config, schema=TEMPLATE_SCHEMA)
    except jsonschema.exceptions.ValidationError as e:
        pytest.fail(f"Test failed: {e}")