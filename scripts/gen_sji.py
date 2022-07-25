#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config
import json

def main():

    print("Generating $name_snake_case$ standard json input file...")

    standard_json_input = $name_pascal_case$.get_verification_info()['standard_json_input']
    abi_file_name = '$name_pascal_case$-$param.project_id$-standard-input.json'
    with open(abi_file_name, 'w') as f:
      f.write(json.dumps(standard_json_input))
    print(abi_file_name, "saved.")
