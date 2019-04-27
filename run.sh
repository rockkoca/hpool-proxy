#!/usr/bin/env bash
if [[ "$#" -ne 1 ]]; then
  echo "Usage: $0 x-account" >&2
  exit 1
fi
python run.py $1
./app/x-proxy-linux-amd64