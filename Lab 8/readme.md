Name - SHYAM MARJIT<br/>
Email - shyam.marjit@iiitg.ac.in<br/>
Roll No - 1901195<br/>
Assignment - 8<br/>

1. Go to the hadoop user.
```sh
$ su - hadoopusr
```
2. Strat the hadoop Hadoop daemons.
```sh
$ start-dfs.sh
```
```sh
$ start-yarn.sh
```
3. Make a directory Assignment8 in our HDFS in the root directory that will store our big.txt file.
```sh
$ hdfs dfs -mkdir /Assignment8
```
4. Copy the big.txt and test.txt file from local to the Assignment8 folder.
```sh
$ hdfs dfs -copyFromLocal /home/shyam/Documents/big.txt /Assignment8
```
```sh
$ hdfs dfs -copyFromLocal /home/shyam/Documents/test.txt /Assignment8
```
5. List down content of the root directory.
```sh
$ hdfs dfs -ls /
```
6. List down content of /Assignment8 folder, there must be big.txt and test.txt file inside it and also it must contain the output.
```sh
$ hdfs dfs -ls /Assignment8
```
7. Go to the folder in which we have the pyhton code to compile the python code using chmod +x.
```sh
	$ cd /home
	$ cd shyam/
	$ cd Documents/
```

# Part - A

8. Here name of the first part program is mappera.py only, compile the python code.
```sh
$ sudo chmod +x mappera.py
```
9. Let’s run our python file with the help of the Hadoop streaming utility.
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/big.txt -output /Assignment8/outputA2 -mapper /home/shyam/Documents/mappera.py
```
10. Show the output.
```sh
$ hdfs dfs -cat /Assignment8/outputA2/part-00000
```
11. Show the sample output with the given example in the Assignment-8 (test.txt).
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/test.txt -output /Assignment8/outputTest -mapper /home/shyam/Documents/mappera.py
```
12. Show the output for the test.txt file.
```sh
$ hdfs dfs -cat /Assignment8/outputTest/part-00000
```
# Part - B
13. Go to the folder in which we have the pyhton code to compile the python code using chmod +x.
```sh
$ cd /home
$ cd shyam/
$ cd Documents/
```
14. Here name of the second part python programs is mapperb.py and reducerb.py
```sh
$ sudo chmod +x mapperb.py reducerb.py
```
15. Let’s run our python file with the help of the Hadoop streaming utility.
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/big.txt -output /Assignment8/outputB -mapper /home/shyam/Documents/mapperb.py -reducer /home/shyam/Documents/reducerb.py
```
16. Show the output.
```sh
$ hdfs dfs -cat /Assignment8/outputB/part-00000
```
17. Show the sample output with the given example in the Assignment-8 (test.txt). Check for the test.txt file whether code are working or not.
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/test.txt -output /Assignment8/outputBTest -mapper /home/shyam/Documents/mapperb.py -reducer /home/shyam/Documents/reducerb.py
```
18. Show the output for the test.txt file.
```sh
$ hdfs dfs -cat /Assignment8/outputBTest/part-00000
```
# Part - C
19. Here name of the second part python programs is mapperb.py, reducerb.py and combiner.py
```sh
$ sudo chmod +x mapperb.py reducerb.py combiner.py
```
20. Let’s run our python file with the help of the Hadoop streaming utility.
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/big.txt -output /Assignment8/outputC -mapper /home/shyam/Documents/mapperb.py -reducer /home/shyam/Documents/reducerb.py -combiner /home/shyam/Documents/combiner.py
```
21. Show the output.
```sh
$ hdfs dfs -cat /Assignment8/outputC/part-00000
```
22. Show the sample output with the given example in the Assignment-8 (test.txt). Check for the test.txt file whether code are working or not.
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/test.txt -output /Assignment8/outputCTest -mapper /home/shyam/Documents/mapperb.py -reducer /home/shyam/Documents/reducerb.py -combiner /home/shyam/Documents/combiner.py
```
23. Show the output for the test.txt file.
```sh
$ hdfs dfs -cat /Assignment8/outputCTest/part-00000
```
# Part - D
24. Here name of the second part python programs is mapperd.py, reducerd.py
```sh
$ sudo chmod +x mapperd.py reducerd.py
```
25. Let’s run our python file with the help of the Hadoop streaming utility.
```sh
$ hadoop jar /home/shyam/Documents/hadoop-streaming-2.7.3.jar -input /Assignment8/big.txt -output /Assignment8/outputD -mapper /home/shyam/Documents/mapperd.py -reducer /home/shyam/Documents/reducerd.py
```
26. Show the output.
```sh
$ hdfs dfs -cat /Assignment8/outputD/part-00000
```
