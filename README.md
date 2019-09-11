# SF Crime Statistics with Spark Streaming

In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

### data_Producer.py
After running the following commands
```
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <your-topic-name> --from-beginning
```

We now lunch the producer_server.py and we should have this expected output
![message](message.png)

### Data streaming
Apache Spark already has an integration with Kafka Brokers, hence we will not need a separate Kafka Consumer.
Implement features in data_stream.py.
Do a spark-submit using this command:

```
 spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0 --master local[4] data_stream.py
``` 

This is what your output would look like

![stream](data.png)

#### Note
Don't forget to initialize your environment variables,It will depend on your your files setup. It should look like this 
```
export SPARK_HOME=/Users/dev/spark-2.3.0-bin-hadoop2.7
```
### Data Source
Please I want to point out the fact that by the time I did this project the database provided by udacity in the resources panel did not match with the starter code. 

In an attempt not to modify the starter code I checked on google for the dataset that was depicted in the starter code. Fortunately for me I found one that matched with the required fields. Below is thye link tto where I took `https://www.kaggle.com/san-francisco/sf-police-calls-for-service-and-incidents/version/61`
