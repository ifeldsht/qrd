ct_url="https://clinicaltrials.gov/ct2/crawl"
log_file=ct_crawler.log

lynx -dump -listonly $ct_url | \
    grep "/ct2/crawl/"       | \
    cut -b 1-6 --complement  | \
    while read list_url
do
    prev=$(grep $list_url $log_file)
    if [ "$prev" == "" ]
    then
        list_id=$(echo $list_url | cut -d'/' -f6)
        mkdir -p $list_id
        lynx -dump -listonly $list_url | \
            grep "/ct2/show/NCT"       | \
            cut -b 1-6 --complement    | \
            while read trial_url        
            do
                trial_id=$(echo $trial_url | cut -d'/' -f6)
                trial_url_desc=$trial_url"?show_desc=Y#desc"
                desc=$(lynx -dump "$trial_url_desc" | \
                 sed 's/^ *//g'                | \
                 sed '/^Detailed Description:$/,/^Eligibility$/{//!b};d')
                out_str=\"trial_url\":\"$trial_url\",
                out_str="{"$out_str\"description\":\"$desc\""}"
                echo $out_str > $list_id/$trial_id".json"
                sleep 0.1
            done
        tar -zcf $list_id".tar.gz" $list_id
        rm -r $list_id
        echo $list_url >> $log_file
    else
        echo "Skipping " $list_url
    fi

done


