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

def test_mint_first_token_is_1($name_snake_case$, accounts):
    tx = $name_snake_case$.mint(accounts[1], {"from": accounts[0]})
    token_id = tx.return_value
    assert token_id == 1

# <% if param.with_max_supply %>
def test_mint_max_supply($name_snake_case$, accounts):
    assert $name_snake_case$.totalSupply() == 0
    assert $name_snake_case$.maxSupply() == MAX_SUPPLY
    with brownie.reverts():
        for i in range(0, MAX_SUPPLY + 1):
            $name_snake_case$.mint(accounts[1], {"from": accounts[0]})
# <% endif %>
