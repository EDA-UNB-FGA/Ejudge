#!/bin/bash
mkdir -p $HOME/ejudge $HOME/bin
rm -rf $HOME/ejudge/bin
cp -rf ejudge_modules/ $HOME/ejudge/bin
cp ejudge ejudge.py $HOME/bin
