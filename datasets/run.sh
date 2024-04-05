#!/bin/bash

apt update && sudo apt upgrade -y
apt install python3.10

pip3 install virtualenv

cd ~/notebooks/
source ~/notebooks/zolo-ai/bin/activate

./zolo-ai/bin/pip3 install ipykernel
python3.10 -m ipykernel install --user --name=zolo-ai

./zolo-ai/bin/pip3 install -r requirements.txt
./zolo-ai/bin/pip3 pip install -q peft bitsandbytes transformers trl ipywidgets widgetsnbextension accelerate

jupyter nbextension enable --py widgetsnbextension