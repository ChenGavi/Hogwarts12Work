import pytest


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        if "add_" in item.nodeid:
            item.add_marker(pytest.mark.add)
