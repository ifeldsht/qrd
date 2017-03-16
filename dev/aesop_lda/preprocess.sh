
for n in {002..147}
do
  echo $n
  txt=$(cat ~/data/read_gov_aesop/$n.txt | tr '\n"!?,.' ' ')
  echo $n"#" $txt >> ~/data/read_gov_aesop/all.txt
done
