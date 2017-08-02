#!/bin/bash
echo "Instalando..."
chmod +x *
mkdir -p $HOME/ejudge $HOME/bin
rm -rf $HOME/ejudge/bin
cp -rf ejudge_modules/ $HOME/ejudge/bin
cp ejudge ejudge.py $HOME/bin
echo "Adicionando ejudge ao PATH..."
printf '\nif [ -d "$HOME/bin" ] ; then' >> ~/.bashrc
printf '\nPATH=$HOME/bin:$PATH' >> ~/.bashrc
printf '\nfi\n' >> ~/.bashrc
source ~/.bashrc
echo "Instalação completa."