import psycopg2

conn = psycopg2.connect(
    dbname='your_db',
    user='your_user',
    password='your_pass',
    host='your-redshift-cluster-url',
    port='5439'
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS processed_sales (
        name VARCHAR(100),
        updated_sales FLOAT
    )
""")

copy_cmd = """
    COPY processed_sales(name, updated_sales)
    FROM 's3://your-s3-bucket-name/output/'
    IAM_ROLE 'arn:aws:iam::your-account-id:role/yourRedshiftRole'
    FORMAT AS CSV
    IGNOREHEADER 1
"""
cursor.execute(copy_cmd)
conn.commit()
print("Data loaded into Redshift.")
cursor.close()
conn.close()

