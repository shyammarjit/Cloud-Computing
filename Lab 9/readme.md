Open a linux terminal<br/>
```sh
sudo su -
```
```sh
cd /opt/spark/
```
```sh
spark-shell
```
Keep this terminal as running and now open a new terminal<br/>
```sh
su - hadoopusr
```
```sh
sudo service ssh start
```
```sh
ssh localhost
```
```sh
start-dfs.sh
```
```sh
start-yarn.sh
```
Run this for only onetime<br/>
```sh
hdfs dfs -mkdir /adult_data
```
go to the folder in which we have the python file<br/>
```sh
hdfs dfs -copyFromLocal /home/shyam/Music/adultdata.txt /adultdata
```
or<br/>
```sh
hdfs dfs -put adultdata.txt /adultdata
```
```sh
hdfs dfs -ls /adultdata
```
