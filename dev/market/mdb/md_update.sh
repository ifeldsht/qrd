python ../../ftpes/ftpes.py info@q-rd.com febr21 md.u.$1.zip
unzip md.u.$1.zip
sudo -u postgres psql -d md -f db_update.sql
rm md.u.$1.zip
rm -r md
