#!/bin/bash
echo "Instalando..."
chmod +x *
mkdir -p $HOME/ejudge $HOME/bin
rm -rf $HOME/ejudge/bin
cp -rf ejudge_modules/ $HOME/ejudge/bin
cp ejudge ejudge.py $HOME/bin
echo "Adicionando ejudge ao PATH..."
export PATH=$PATH:$HOME/bin
echo $PATH
echo "Feche e abra o terminal para finalizar a instalação..."