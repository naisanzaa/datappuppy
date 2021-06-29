#!/bin/bash

cd $(dirname $0) && set -xe

python3 main.py

exec $@
