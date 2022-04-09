while read p; do
  curl "$p"  >> new.txt;
done < few_links.txt
