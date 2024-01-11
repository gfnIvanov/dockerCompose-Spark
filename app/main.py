from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local[*]")\
        .appName('SPARK_PG')\
        .config("spark.jars", "/opt/spark-apps/drivers/postgresql-42.7.1.jar") \
        .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://db:5432/spark_db") \
    .option("dbtable", "house_prices") \
    .option("user", "postgres") \
    .option("password", "root") \
    .option("driver", "org.postgresql.Driver") \
    .load()


df.createOrReplaceTempView("house_prices")

spark.sql("""select avg(price),
                    location, 
                    bedrooms
               from house_prices
             group by location, bedrooms""").show()
