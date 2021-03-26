sudo chmod -R 777 **/*

echo "Installing Python...." 
sudo yum install -y python3

echo "Installing pip...." 
yes | sudo yum install python-pip

echo "Installing setuptools..."
yes | sudo yum install gcc

sudo pip3 install --upgrade pip

echo "Changing directory to backend-app/ ..."
cd backend-app

echo "Installing requirements...."
pip3 install -r requirements.txt

echo "Changing directory to scripts/ ..."
cd scripts

python3 time.py 
# ec2