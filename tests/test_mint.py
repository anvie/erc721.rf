#!/usr/bin/python3
import pytest
import brownie

from consts import *

import pytest
import brownie


def test_mint($name_snake_case$, accounts):
    tx = $name_snake_case$.mint(accounts[1], {"from": accounts[0]})
    token_id = tx.return_value
    assert $name_snake_case$.ownerOf(token_id) == accounts[1]