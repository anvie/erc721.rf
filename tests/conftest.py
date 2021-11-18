#!/usr/bin/python3

from brownie import config
import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def $name_snake_case$($name_pascal_case$Test, accounts):
    _$name_snake_case$ = $name_pascal_case$Test.deploy("https://$name_snake_case$.com/metadata/", {'from': accounts[0]})
    return _$name_snake_case$

