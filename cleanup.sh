#!/bin/bash
find . -name '*~' -exec rm -rf {} \;
find . -name '*.pyc' -exec rm -rf {} \;
