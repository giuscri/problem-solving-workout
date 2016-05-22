cat data.txt |
sort |
uniq -c |
egrep '^\s+1[^0-9]' |
sed -r 's,^\s+,,' |
cut -f 2 -d ' '
