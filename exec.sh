#!/bin/bash

function convert_directory() {
  BASE=$1
  mkdir -p $BASE-ja
  echo "ls $BASE/*.md | xargs -I{} basename {} | xargs -I{} python convert.py -i $BASE/{} -o $BASE-ja/{}"
        ls $BASE/*.md | xargs -I{} basename {} | xargs -I{} python convert.py -i $BASE/{} -o $BASE-ja/{}
}

function convert_file() {
  BASE=$1
  echo "python convert.py -i $BASE.md -o $BASE-ja.md"
        python convert.py -i $BASE.md -o $BASE-ja.md
}

convert_directory docs/spec/v1.0
convert_file docs/provenance/v1
