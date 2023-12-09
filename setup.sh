#!/bin/bash

dotfilesdir="$PWD"

for config in *; do
  if [ -d "$config" ]
  then
    echo "Setting up: $config"
    cd $config
    sh setup.sh || echo "Failed to setup $config"
    cd $dotfilesdir
  fi
done