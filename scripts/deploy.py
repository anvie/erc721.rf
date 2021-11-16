#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config


def main():
    print("Deploying $name$...")
    return $name_pascal_case$.deploy("https://$name_snake_case$.xyz/metadata/", {'from': accounts[0]})
