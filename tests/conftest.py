#!/usr/bin/python3

from brownie import config
import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def root(accounts):
    acc = accounts.add(config['wallets']['root_key'])
    return acc

@pytest.fixture(scope="module")
def admin(accounts):
    acc = accounts.add(config['wallets']['admin_key'])
    return acc

@pytest.fixture(scope="module")
def $name_snake_case$($name_pascal_case$Test, root, admin):
    _$name_snake_case$ = $name_pascal_case$Test.deploy("https://$name_snake_case$.com/metadata/", root, admin, {'from': root})
    return _$name_snake_case$

