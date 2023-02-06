from celery import shared_task

@shared_task
def load_server_to_mysql(file_path: str):
    from pyspark.sql import SparkSession
    from pyspark.sql.types import (
        StructType,
        StringType,
        StructField,
        IntegerType,
    )

    spark = SparkSession.builder.master("local[*]").appName("yc_local").getOrCreate()
    schema = StructType([
        StructField("name", StringType(), True),
        StructField("alias_name", StringType(), True),
        StructField("ip", StringType(), True),
        StructField("user", StringType(), True),
        StructField("password", StringType(), True),
        StructField("ssh_public_key_path", StringType(), True),
        StructField("ssh_private_key_path", StringType(), True),
        StructField("is_deleted", IntegerType(), True),
        StructField("add_date", StringType(), True),
        StructField("org_id", IntegerType(), True),
    ])
    df = spark.read.csv(
        path=f"file://{file_path}",
        sep=",",
        header=False,
        schema=schema,
    )

    df.show()
    df.write.jdbc(
        url="jdbc:mysql://node2:3306/codebox?useSSL=false&useUnicode=true&characterEncoding=UTF-8",
        table="jmp_host",
        mode="append",
        properties={"user": "xxx", "password": "xxx"}
    )

    spark.stop()