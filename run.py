#!/bin/bash

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: run.py x-account")
    account = f'"X-Account": "{sys.argv[1]}"'
    filename = 'app/proxy.conf'
    with open(filename, 'r') as file:
        content = file.read()

    with open('proxy.conf', 'w') as file:
        file.write(content.replace('"X-Account": ""', account))
