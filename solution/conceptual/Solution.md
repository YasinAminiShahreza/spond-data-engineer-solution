## Question 1.1 - Data ingestion
As it's been some time that I haven't used AWS and it can evolve over time and there might be updates or changes since then. For this reason, to make sure my answers are accurate, I assume the cloud providers is Microsoft Azure. 

The operation of data injestion can be either of the following forms. Either real-time injestion or Batch Injestion.

# Real-time Injestion
For the real time injestion, you can use Azure Stream Analytics, Azure Event Hubs and Azure Data Explorer. 

Azure Stream Analytics: It's a serverless and fully manages service to process and analyze real time data. You can process using SQL queries and save the output data in SQL data base, Cosmos db and Azure data lake storage. You might need to consider using AVRO for effeicent write operations dependeing on the frequency of the data. On the other hand if you would rather to have more read-optimized data, you might consider outputing the data into the Parquete.


Azure Event Hubs: This service can be used for reciving real-time data from multiple devices, sensors and event based applications. It's possible to integrate it with Azure Stream Analytics and use the SQL-liked Query language for real time processing and analysis.

Azure Data Explorer: It's designed to injest large volume of real-time data and prcessing them on the fly. This is mostly used for logs and telementary data though however with the more updates coming out, it's getting as popluar as Strean Analytics. 

# Bacth Injestion:

Azure Data Factory: It is the best tool for the batch opearion. It provides safe connection to different Azure services using managed identity for data injestion. It's possible to interact with Azure Event Grid to configure event based bacth analysis so the pipelines can be run manually, event based, scheduled based or API trigger.

# Do you need transformation?:

Then you might have to consider Azure Function, Data Bricks or Azure Batch Serives.

Azure Fucnions: It's a serverless service to run your code snippit and very cost-effective especially batch operaions.(This service doesn't support R, you might wanna choose Azure Data Bricks or Batch Service)

Data Bricks: It is built on top of Apache Spark and designed to simplify the process and transforamtion of building big data solutions. It supports multiple languages inclusing R, Python and Scala.

Azure Batch Serice: This is partially managed VM that you have more control on the underlying OS than Data Bricks and Azure Fucntions. This gives you the highest freedom of language, operarion and dependecnies configuration. This freedom comes with a cost of having to maintain the servers including updates, patching and security monitoring.

Note: Azure Snyapse Analytcs is a ceterlized service relaesed recently that can embed multiple solutions from injestion to processing and providing data warehouse with dedicated SQL pools.


# Netowrk Issues on the data processing?:

There might many different network issues you face during data processing. These could be firewalls issues which are the most comman, packet delivery(using UDP protocols), assiging networks, subnets and gateways and might be sometimes latency (this can be by bandwidth, physical issues like sharp angle in the Fiber optics cables and etc)

# Costs:
There factors on how to control the costs such as administrative managments, how much an application is bussines critical, In case of batch jobs, how often you want to run them and etc.
For example for a scenrario that you might want to run parrallel batch jobs often(multiple times during the day), you might wanna use Batch service or in other words dedicated vm's with reserved instances to save costs. You can reserve CPU and storage in advance for 1 - 3 years contract and it can save up to 50% compareed to running the code on instant intances. 

# Pro tip:
Both running stream and batch services, you might wanna use your own costumized image, you can build your image via github actions only if dependenices has changed, and restore in the container registries for your machine configuration that supposed to run your code. Similarly, you make your Kubernetes clusters by loading the verified image from either github/Azure registeris into your Dockerfile. 


## Question 1.2 - Data transformation and cleaning

As I mentioned above, the most commona ways of Data processing in Azure is Azure Data Factory on the module of Data Flow for the simple logic transformation.Azure Data Flow of Data Factory provides a easy to use UI to control and monitor the data flow and quality for simple transforamtion.For more complex operations Data Bricks, Batch services, Azure functions or simply a virtual machine for complex code based processing and transforamtion. 

SPARK and MapReduce are the most common framework for big data analysis. SPARK is the most recent technology and can handle wider variaty of data types and it supports not only HDFS but also data stored in variaty of formats including Cassandra and blob storage and Data lakes.(S3 buckets in AWS). It is also X100 fatser than MR and it does the calcualtion mostly in the memory but it can spill into the disk if memoery fills up. The core of SPARK is RDD in which the opeartions are lazy evaluated.
Worth to mention that MapReduce only allows computation on the HDFS files and Task tracker dedicates CPU and RAM for executions.

For Schema evolution, mostly the documetation and Schema versioning are the first choice. Using structured databases like SQL ensures that the data are consitent but on the other hand there are more works to be done to define new Schemas in case of further evolution. Some examples of data quality issues can be missing values, duplicated rows, wrong Schema definition (int, float and string) and the solution for most of them are creating logs of data that don't pass consitency tests and go through them manually or programmatically. Consistency tests can be code snippits that verify the end result before loading them into a data Warehouse during ETL operations. 


The questions are quite general and it's possible to write more about them but I tried to convey the main concepts. 








