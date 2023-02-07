import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf

def executeSQLFile(filename):
    with open(r'/root/airflow/data/sql/' + filename, 'r') as f:
        read_data = f.readlines()
    # 将数组的一行一行拼接成一个长文本，就是SQL文件的内容
    read_data = ''.join(read_data)
    # 将文本内容按分号切割得到数组，每个元素预计是一个完整语句
    arr = read_data.split(";")
    # 对每个SQL,如果是空字符串或空文本，则剔除掉
    # 注意，你可能认为空字符串''也算是空白字符，但其实空字符串‘’不是空白字符 ，即''.isspace()返回的是False
    arr2 = list(filter(lambda x: not x.isspace() and not x == "", arr))
    # 对每个SQL语句进行迭代
    for sql in arr2:
        # 先打印完整的SQL语句。
        print(sql, ";")
        # 由于SQL语句不一定有意义，比如全是--注释;，他也以分号结束，但是没有意义不用执行。
        # 对每个SQL语句，他由多行组成，sql.splitlines()数组中是每行，挑选出不是空白字符的，也不是空字符串''的，也不是--注释的。
        # 即保留有效的语句。
        filtered = filter(lambda x: (not x.lstrip().startswith("--")) and (not x.isspace()) and (not x.strip() == ''),
                          sql.splitlines())
        # 下面数组的元素是SQL语句有效的行
        filtered = list(filtered)

        # 有效的行数>0，才执行
        if len(filtered) > 0:
            df = spark.sql(sql)
            # 如果有效的SQL语句是select开头的，则打印数据。
            if filtered[0].lstrip().startswith("select"):
                df.show(100)

def register_udf():
    pass

if __name__ == '__main__':
    os.environ["JAVA_HOME"] = "/usr/java/jdk1.8.0_181-cloudera"
    os.environ["HADOOP_CONF_DIR"] = "/etc/hadoop/conf"
    os.environ["YARN_CONF_DIR"] = "/etc/hadoop/conf"
    os.environ["PYSPARK_PYTHON"] = "/root/anaconda3/envs/spark/bin/python3"
    os.environ["PYSPARK_DRIVER_PYTHON"] = "/root/anaconda3/envs/spark/bin/python3"
    print("---开始执行dwd app层etl任务---")

    # 1) 创建 sparkSession对象, 此对象支持连接hive
    # .master("local[*]") \
    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("insurance_main") \
        .config("spark.sql.shuffle.partitions", 200) \
        .config("spark.sql.warehouse.dir", "hdfs://node03:8020/user/hive/warehouse") \
        .config("hive.metastore.uris", "thrift://node03:9083") \
        .config("spark.sql.hive.metastore.jars", "/opt/cloudera/parcels/CDH-6.3.1-1.cdh6.3.1.p0.1470567/lib/hive/lib/*") \
        .config("spark.sql.hive.metastore.version", "2.1.1") \
        .config("spark.pyspark.driver.python", "/root/anaconda3/envs/spark/bin/python3") \
        .config("spark.pyspark.python", "/root/anaconda3/envs/spark/bin/python3") \
        .enableHiveSupport() \
        .getOrCreate()

    register_udf()
    executeSQLFile('dwd.sql')
    executeSQLFile('app.sql')

    app_alertmanager_user_result_df = spark.sql("""
        select * from goldfish_app.app_alertmanager_user_result
    """)

    app_alertmanager_user_result_df.write.jdbc(
        url="jdbc:mysql://node02:3306/codebox?createDatabaseIfNotExist=true&serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=UTF-8",
        table="app_alertmanager_user_result",
        mode="append",
        properties={"user": "yc", "password": "zzyycc1013"}
    )


    app_alertmanager_job_result_df = spark.sql("""
            select * from goldfish_app.app_alertmanager_job_result
        """)

    app_alertmanager_job_result_df.write.jdbc(
        url="jdbc:mysql://node02:3306/codebox?createDatabaseIfNotExist=true&serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=UTF-8",
        table="app_alertmanager_job_result",
        mode="append",
        properties={"user": "yc", "password": "zzyycc1013"}
    )


    app_alertmanager_job_status_result_df = spark.sql("""
            select * from goldfish_app.app_alertmanager_job_status_result
        """)

    app_alertmanager_job_status_result_df.write.jdbc(
        url="jdbc:mysql://node02:3306/codebox?createDatabaseIfNotExist=true&serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=UTF-8",
        table="app_alertmanager_job_status_result",
        mode="append",
        properties={"user": "yc", "password": "zzyycc1013"}
    )


    spark.stop()