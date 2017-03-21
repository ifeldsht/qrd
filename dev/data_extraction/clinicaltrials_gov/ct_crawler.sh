ct_url="https://clinicaltrials.gov"
search_url=$ct_url"/ct2/results?term=cancer&pg="

for page in {2..2}
do
  echo $page

  lynx -listonly -dump $search_url$page | \
      grep "gov/ct2/show"               | \
      cut -b 1-6 --complement           | \
      while read trial_url
  do
    out_str=\"trial_url\":\"$trial_url\",
    
    desc=$(lynx -dump $trial_url | \
      sed 's/^ *//g'             | \
      sed '/^Detailed Description:$/,/^Eligibility$/{//!b};d')

    out_str=$out_str\"description\":\"$desc\",

    purp=$(lynx -dump $trial_url | \
      sed 's/^ *//g'             | \
      sed '/^Purpose$/,/^\[.*\]Condition$/{//!b};d')

    out_str=$out_str\"purpose\":\"$purp\"

    counter=0
    abs_str="\"abstracts\":["
    lynx -listonly -dump $trial_url | \
      grep "/ct2/bye"               | \
      cut -b 1-6 --complement       | \
      while read url_abs
      do
        #echo $url_abs
        abst=$(lynx -dump $url_abs  | \
          sed 's/^[ ]*//g'          | \
          sed '/^Abstract$/,/^PMID:$/{//!b};d')
        if ((counter>0))
        then
          abs_str=$abs_str","
        fi
        ((counter++))
        abs_str=$abs_str"{\"abstract_url\":\""$url_abs"\","
        abs_str=$abs_str"\"abstract\":\""$abst"\"}"
      done
      abs_str=$abs_str"]"
      echo "{"$out_str $abs_str"}" > a.txt
      exit
  done
done
