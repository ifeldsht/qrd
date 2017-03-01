sudo add-apt-repository ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer

sudo apt-get -y install python-pip python-dev
sudo apt-get -y install git
sudo apt-get -y install zip unzip
sudo apt-get -y install screen
sudo apt-get -y install vim
sudo apt-get -y install apache2

sudo pip install numpy
sudo pip install scipy
sudo pip install matplotlib 
sudo pip install -U scikit-learn
sudo pip install pandas
sudo pip install tensorflow
sudo pip install flask flask-cors
sudo pip install requests

curl -O http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip
unzip stanford-corenlp-full-2016-10-31.zip
mv stanford-corenlp-full-2016-10-31 corenlp
rm stanford-corenlp-full-2016-10-31.zip


