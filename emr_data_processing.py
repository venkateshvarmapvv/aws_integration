from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ProcessSales").getOrCreate()
df = spark.read.csv("s3://your-s3-bucket-name/data/sample_data.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("sales")
result = spark.sql("SELECT name, sales * 1.1 AS updated_sales FROM sales")
result.write.option("header", True).csv("s3://your-s3-bucket-name/output/")

print("Processing completed and result saved to S3.")
spark.stop()

