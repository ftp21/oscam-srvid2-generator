egrep -A1 '^([0-9a-f]{1,4}):eeee0000' lamedb | grep -v "^--" |  cut -d':' -f1  |  awk '{if (e) {print p$0"|||Sky DTT";} else {p=$0":1805@000000|";} e=!e;}'
