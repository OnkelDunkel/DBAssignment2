#!/bin/sh
echo hllo world
sed -i '1s;^;polarity,id,date,query,user,text\n;' testdata.manual.2009.06.14.csv
sed -i '1s;^;polarity,id,date,query,user,text\n;' training.1600000.processed.noemoticon.csv
