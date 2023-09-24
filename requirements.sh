#This script is for Linux users to install the dependencies and run the program
sudo apt-get install scrot
sudo apt-get install python3-tk python3-dev
sudo apt install python3.10-venv
python3 -m venv candyenv
source candyenv/bin/activate
pip install -r requirements.txt
deactivate