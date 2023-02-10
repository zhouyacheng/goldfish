import os
from pyspark.sql import SparkSession


def init_spark():
    os.environ["JAVA_HOME"] = "/usr/java/jdk1.8.0_181-cloudera"
    os.environ["HADOOP_CONF_DIR"] = "/etc/hadoop/conf"
    os.environ["YARN_CONF_DIR"] = "/etc/hadoop/conf"
    os.environ["PYSPARK_PYTHON"] = "/root/anaconda3/envs/spark/bin/python3"
    os.environ["PYSPARK_DRIVER_PYTHON"] = "/root/anaconda3/envs/spark/bin/python3"

    hudi_jar_path = "/root/anaconda3/envs/spark/lib/python3.8/site-packages/pyspark/jars/hudi-spark3.1-bundle_2.12-0.11.1.jar"
    metastore_uri = "thrift://node03:9083"

    hudi_options = {
        "hoodie.table.name": hudi_table_name,
        "hoodie.datasource.write.recordkey.field": record_key,
        "hoodie.datasource.write.table.name": hudi_table_name,
        "hoodie.datasource.write.operation": write_operation,
        "hoodie.datasource.write.precombine.field": precombine_key,
        "hoodie.datasource.write.table.type": write_table_type,
        "hoodie.upsert.shuffle.parallelism": 2000,
        "hoodie.bulkinsert.shuffle.parallelism": 2000,
        "hoodie.insert.shuffle.parallelism": 2000,
        "hoodie.cleaner.policy": "KEEP_LATEST_COMMITS",
        "hoodie.cleaner.fileversions.retained": 6,
        "hoodie.parquet.max.file.size": 1024 * 1024 * 100,
        "hoodie.parquet.small.file.limit": 1024 * 1024 * 60,
        "hoodie.parquet.compression.codec": "snappy",
        "hoodie.bloom.index.parallelism": 4321,
        "hoodie.datasource.write.payload.class": "org.apache.hudi.common.model.DefaultHoodieRecordPayload",
        "hoodie.datasource.hive_sync.mode": "hms",
        "hoodie.datasource.hive_sync.enable": "true",
        "hoodie.datasource.hive_sync.database": db_name,
        "hoodie.datasource.hive_sync.table": hudi_table_name,
        "hoodie.datasource.hive_sync.jdbcurl": "jdbc:hive2://node03:9083",
        "hoodie.datasource.write.hive_style_partitioning": "true",
        "hoodie.datasource.hive_sync.metastore.uris": "thrift://node03:9083",
        "hoodie.datasource.hive_sync.partition_extractor_class": "org.apache.hudi.hive.MultiPartKeysValueExtractor",
    }

    spark = (
        SparkSession.builder.master("local[*]")
        .appName("yc_local")
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config(
            "spark.sql.extensions",
            "org.apache.spark.sql.hudi.HoodieSparkSessionExtension",
        )
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
    return (spark, hudi_options)


if __name__ == "__main__":
    host = os.environ.get("MYSQL_HOST","")
    user = os.environ.get("MYSQL_USER","")
    password = os.environ.get("MYSQL_PASSWORD","")
    table_name = "alertmanager_project"
    hudi_table_name = "alertmanager_project"
    db_name = "new_goldfish_ods"
    path = f"/user/hive/warehouse/{db_name}.db/{hudi_table_name}"
    write_table_type = "MERGE_ON_READ"  # COPY_ON_WRITE
    write_operation = "upsert"
    record_key = "id,name"
    precombine_key = "create_time"
    partition_path = "create_time"
    # spark.sparkContext.setLogLevel("INFO")
    spark, hudi_options = init_spark()

    df = spark.read.jdbc(
        url=f"jdbc:mysql://{host}:3306/codebox?createDatabaseIfNotExist=true&serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=UTF-8",
        table=table_name,
        properties={"user": user, "password": password},
    )
    df.createOrReplaceTempView("t1")
    filter_df = spark.sql(
        """select id,name,role,user_id,create_time from t1"""
    )
    filter_df.show()
    filter_df.write.format("hudi").options(**hudi_options).mode("append").save(path)
    spark.stop()
