#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config
import json

BASE_URL="https://meta.chainbox.id/$param.project_id$/"

def main():
    deployer = accounts.add(config['wallets']['deployer_key'])
    # admin = accounts.add(config['wallets']['admin_key'])
    owner_address = config['wallets']['owner_address']

    print("Deploying $name_snake_case$-contract...")
    print("using deployer key:", deployer.address)

    print("Deploying $name$...")
    contract = $name_pascal_case$.deploy(BASE_URL, owner_address, owner_address, {'from': deployer})

    print("Contract address:", contract.address)

    standard_json_input = $name_pascal_case$.get_verification_info()['standard_json_input']
    with open('$name_pascal_case$-ABI.json', 'w') as f:
      f.write(json.dumps(standard_json_input))
    print("$name_pascal_case$-ABI.json saved.")
