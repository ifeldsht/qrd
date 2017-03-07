for n in {002..147}
do
echo $n
curl -s http://read.gov/aesop/$n.html | sed -n 's:.*<p>\(.*\)</p>.*:\1:p' > ~/data/read_gov_aesop/$n.txt
done

