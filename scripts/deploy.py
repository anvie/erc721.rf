#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config
import json

BASE_URL="https://meta.chainbox.id/$param.project_id$/"

def main():
    owner = accounts.add(config['wallets']['owner_key'])
    admin = accounts.add(config['wallets']['admin_key'])

    print("Deploying $name_snake_case$-contract...")
    print("using owner key:", owner.address)

    print("Deploying $name$...")
    contract = $name_pascal_case$.deploy(BASE_URL, admin, {'from': owner}, publish_source=config['publish_source'])

    print("Contract address:", contract.address)

    standard_json_input = $name_pascal_case$.get_verification_info()['standard_json_input']
    abi_file_name = '$name_pascal_case$-$param.project_id$-standard-input.json'
    with open(abi_file_name, 'w') as f:
      f.write(json.dumps(standard_json_input))
    print(abi_file_name, "saved.")
