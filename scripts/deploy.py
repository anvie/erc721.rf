#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config


def main():
    owner = accounts.add(config['wallets']['owner_key'])
    admin = accounts.add(config['wallets']['admin_key'])

    print("Deploying $name_snake_case$-contract...")
    print("using owner key:", owner.address)

    print("Deploying $name$...")
    return $name_pascal_case$.deploy("https://meta.chainbox.id/$param.project_id$/", admin, {'from': owner})
