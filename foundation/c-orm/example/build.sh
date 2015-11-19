#!/bin/bash

pushd src
PYTHONPATH=../../cgen/src python ../../cgen/src/isti/cgen/run.py foo.h

