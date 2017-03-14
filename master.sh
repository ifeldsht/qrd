sudo add-apt-repository ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer

sudo apt-get -y install python-pip python-dev
sudo apt-get -y install git
sudo apt-get -y install zip unzip
sudo apt-get -y install screen
sudo apt-get -y install vim
sudo apt-get -y install apache2
sudo apt-get -y install awscli
sudo apt-get -y install maven
sudo apt-get -y install postgresql postgresql-contrib

sudo pip install numpy
sudo pip install scipy
sudo pip install matplotlib 
sudo pip install -U scikit-learn
sudo pip install pandas
sudo pip install tensorflow
sudo pip install flask flask-cors
sudo pip install requests
sudo pip install gensim

curl -O http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip
unzip stanford-corenlp-full-2016-10-31.zip
mv stanford-corenlp-full-2016-10-31 corenlp
sudo mv corenlp /opt
rm stanford-corenlp-full-2016-10-31.zip

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt-get install -y mongodb

curl -O http://mirror.cc.columbia.edu/pub/software/apache/nutch/1.12/apache-nutch-1.12-bin.zip
unzip apache-nutch-1.12-bin.zip 
mv apache-nutch-1.12 nutch
sudo mv nutch /opt 
