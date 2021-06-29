#!/bin/bash

# build

cd $(dirname $0) && set -xe

if [ -f ../env.sh ]; then
  docker run -it --env-file ../env.sh datapuppy/analysis $@
else
  docker run -it datapuppy/analysis $@
fi
