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
    desc=$(lynx -dump $trial_url | \
      sed 's/^ *//g'             | \
      sed '/^Detailed Description:$/,/^Eligibility$/{//!b};d')
    purp=$(lynx -dump $trial_url | \
      sed 's/^ *//g'             | \
      sed '/^Purpose$/,/^\[.*\]Condition$/{//!b};d')
    echo "======================================" >> a.txt
    lynx -listonly -dump $trial_url | \
      grep "/ct2/bye"               | \
      cut -b 1-6 --complement       | \
      while read url_abs
      do
        abst=$(lynx -dump $url_abs  | \
          sed '/^Abstract$/,/^KEYWORDS:$/{//!b};d')
        echo $abst 
      done
  done
done
