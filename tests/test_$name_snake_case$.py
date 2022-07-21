#!/usr/bin/python3
import pytest
import brownie

from consts import *

import pytest
import brownie


def test_owner_admin($name_snake_case$, owner, admin):
    assert $name_snake_case$.owner() == owner
    assert $name_snake_case$.admin() == admin

def test_supports_interface($name_snake_case$, owner, admin):
    assert $name_snake_case$.supportsInterface("0x01ffc9a7") == True
    assert $name_snake_case$.supportsInterface("0x80ac58cd") == True
    assert $name_snake_case$.supportsInterface("0xffffffff") == False

def test_total_supply($name_snake_case$, accounts):
    assert $name_snake_case$.totalSupply() == 0
    $name_snake_case$.mint(accounts[3], {"from": accounts[3]})
    assert $name_snake_case$.totalSupply() == 1

@pytest.mark.parametrize("idx", range(1, 10))
def test_total_supply_increased($name_snake_case$, accounts, idx):
    assert $name_snake_case$.totalSupply() == 0
    for i in range(idx):
        $name_snake_case$.mint(accounts[3], {"from": accounts[3]})
    assert $name_snake_case$.totalSupply() == idx

# Test code for ERC721Enumerable
# uncomment this code if your contract use ERC721Enumerable extension
#@pytest.mark.parametrize("idx", range(1, 10))
#def test_token_enumerate($name_snake_case$, accounts, idx):
#    assert $name_snake_case$.totalSupply() == 0
#    for i in range(0, idx):
#        $name_snake_case$.mint(accounts[3], {"from": accounts[3]})
#        assert $name_snake_case$.tokenByIndex(i) == i + 1

def test_base_uri($name_snake_case$, admin):
    assert $name_snake_case$.baseTokenURI() == "https://$name_snake_case$.one/meta/"
    $name_snake_case$.mint(admin, {"from": admin})
    assert $name_snake_case$.tokenURI(1) == "https://$name_snake_case$.one/meta/1"




# @TODO(you): add tests here
