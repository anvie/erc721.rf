#!/usr/bin/python3

import pytest
import brownie


def test_change_root($name_snake_case$, accounts):
    $name_snake_case$.changeRoot(accounts[1], {"from": accounts[0]})
    assert $name_snake_case$.root() == accounts[1]

def test_change_admin($name_snake_case$, accounts):
    $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[0]})
    assert $name_snake_case$.admin() == accounts[1]

def test_only_root_can_change_admin($name_snake_case$, accounts):
    with brownie.reverts():
        $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[1]})
    
    $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[0]})

    # admin cannot change admin
    with brownie.reverts():
        $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[1]})

    $name_snake_case$.changeRoot(accounts[1], {"from": accounts[0]})
    $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[1]})
