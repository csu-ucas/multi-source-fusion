echo "Start installing dependencies"
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
git clone https://github.com/szazo/DHT11_Python
python3 -m pip install DHT11_Python

pip3 install -r requirements.txt

echo "Start installing opencv........."
sh ./installOpenCV.sh -x

sudo apt install -y libatlas-base-dev
sudo apt install -y libjasper-dev
sudo apt install -y libqt4-test libqtgui4
sudo apt install -y libhdf5-dev libhdf5-serial-dev

echo "
export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1" >> ~/.bashrc
source ~/.bashrc

echo "Dependencies has been installed" > .install-log.log 