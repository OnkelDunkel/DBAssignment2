# intro
While developing i used the test data which worked very nicely. When i tried with the full data it messed my computer so I did not manage to answer the questions for the big data.
# How to
Due my PC getting messed up I did not get to set it up nicely with a docker container. However it should still be possible to make it work if you have mongodb running on your computer. These are the steps:

1. download twitter data from http://help.sentiment140.com/for-students/ and extract the files
2. run below command from the same folder as the csv files.

	mongoimport -d twitter_db -c tweets --type csv --file testdata.manual.2009.06.14.csv --headerline
	
3. from same folder as twitter_db.py run below command:
	
	python3 hello.py