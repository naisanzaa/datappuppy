#!/bin/bash

# test

cd $(dirname $0) && set -xe

bash build.sh

docker run -it datapuppy/analysis $@
