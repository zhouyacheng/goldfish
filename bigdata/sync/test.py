import datetime
import os
from pyspark.sql import SparkSession

os.environ["JAVA_HOME"] = "/usr/java/jdk1.8.0_181-cloudera"
os.environ["HADOOP_CONF_DIR"] = "/etc/hadoop/conf"
os.environ["YARN_CONF_DIR"] = "/etc/hadoop/conf"
os.environ["PYSPARK_PYTHON"] = "/root/anaconda3/envs/spark/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/root/anaconda3/envs/spark/bin/python3"

hudi_jar_path = "/root/anaconda3/envs/spark/lib/python3.8/site-packages/pyspark/jars/hudi-spark3.1-bundle_2.12-0.11.1.jar"
metastore_uri = "thrift://node03:9083"

spark = (
    SparkSession.builder.master("local[*]")
    .appName("yc_local")
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .config("spark.sql.extensions", "org.apache.spark.sql.hudi.HoodieSparkSessionExtension")
    .config("spark.jars", hudi_jar_path)
    .config("spark.driver.extraClassPath", hudi_jar_path)
    .config("hive.metastore.uris", metastore_uri)
    .config("spark.sql.warehouse.dir", "hdfs://node03:8020/user/hive/warehouse")
    .config("hive.metastore.uris", "thrift://node03:9083")
    # .config("spark.sql.hive.metastore.jars", "/opt/cloudera/parcels/CDH-6.3.1-1.cdh6.3.1.p0.1470567/lib/hive/lib/*")
    .config("spark.sql.hive.metastore.version", "2.1.1")
    .config("spark.pyspark.driver.python", "/root/anaconda3/envs/spark/bin/python3")
    .config("spark.pyspark.python", "/root/anaconda3/envs/spark/bin/python3")
    .enableHiveSupport()
    .getOrCreate()
)
# spark.sparkContext.setLogLevel("INFO")
df = spark.read.jdbc(
        url="jdbc:mysql://node02:3306/codebox?createDatabaseIfNotExist=true&serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=UTF-8",
        table="app_alertmanager_job_status_result",
        properties={"user": "xxx", "password": "xxx"}
    )

df.show()
"""
dataframe_mysql = spark.read\
    .format("jdbc")\
    .option("url", "jdbc:mysql://localhost/database_name")\
    .option("driver", "com.mysql.jdbc.Driver")\
    .option("dbtable", "employees").option("user", "root")\
    .option("password", "12345678").load()
"""

# table_name = "hudi_0_11_0_test"
# db_name = "user_test"
# path = f"/user/hive/warehouse/{db_name}.db/{table_name}"
# # path = f"/tmp/{table_name}"
# hudi_options = {
#     'hoodie.table.name': table_name,
#     'hoodie.datasource.write.recordkey.field': "k1,k2",
#     'hoodie.datasource.write.table.name': table_name,
#     'hoodie.datasource.write.operation': "upsert",
#     'hoodie.datasource.write.precombine.field': "cmp_key",
#     # 'hoodie.datasource.write.table.type': "COPY_ON_WRITE",
#     'hoodie.datasource.write.table.type': "MERGE_ON_READ",
#     'hoodie.upsert.shuffle.parallelism': 2000,
#     'hoodie.bulkinsert.shuffle.parallelism': 2000,
#     'hoodie.insert.shuffle.parallelism': 2000,
#     'hoodie.cleaner.policy': 'KEEP_LATEST_COMMITS',
#     'hoodie.cleaner.fileversions.retained': 6,
#     'hoodie.parquet.max.file.size': 1024*1024*100,
#     'hoodie.parquet.small.file.limit': 1024*1024*60,
#     'hoodie.parquet.compression.codec': 'snappy',
#     'hoodie.bloom.index.parallelism': 4321,
#     'hoodie.datasource.write.payload.class': "org.apache.hudi.common.model.DefaultHoodieRecordPayload",
#     'hoodie.datasource.hive_sync.mode': "hms",
#     'hoodie.datasource.hive_sync.enable': 'true',
#     'hoodie.datasource.hive_sync.database': db_name,
#     'hoodie.datasource.hive_sync.table': table_name,
#     'hoodie.datasource.hive_sync.jdbcurl': "jdbc:hive2://node03:9083",
#     'hoodie.datasource.write.hive_style_partitioning': "true",
#     'hoodie.datasource.write.partitionpath.field': "pt1,pt2",
#     # 'hoodie.datasource.hive_sync.username': "root",
#     # 'hoodie.datasource.hive_sync.password': "123456",
#     "hoodie.datasource.hive_sync.metastore.uris": "thrift://node03:9083",
#     'hoodie.datasource.hive_sync.partition_extractor_class': 'org.apache.hudi.hive.MultiPartKeysValueExtractor',
#     'hoodie.datasource.write.keygenerator.class': 'org.apache.hudi.keygen.ComplexKeyGenerator'
# }
# # df.write.format("hudi").options(**hudi_options).mode("overwrite").save(path)
# df.write.format("hudi").options(**hudi_options).mode("append").save(path)

spark.stop()