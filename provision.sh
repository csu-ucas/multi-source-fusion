pip3 install -r 
sh ./installOpenCV.sh -x
apt install libatlas-base-dev
apt install libjasper-dev
apt install libqt4-test libqtgui4
apt install libhdf5-dev libhdf5-serial-dev

echo "
export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1" >> ~/.bashrc
source ~/.bashrc
