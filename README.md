apt-get upgrade -y
apt-get update -y
pkg upgrade -y
pkg update -y 
pkg install nodejs -y 
pkg install nodejs-lts -y
pkg install ffmpeg -y 
pkg install wget -y 
pkg install tesseract -y
pkg install git -y
termux-setup-storage
git clone https://github.com/REND3RO/InstaBanTool
cd InstaBanTool 
chmod +x *
python igban.py
