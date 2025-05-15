# AWS Data Pipeline Demo

This project demonstrates a basic AWS data pipeline:
- Uploads CSV to S3
- Processes it using PySpark on EMR
- Loads results to Amazon Redshift

## Files
- `s3_upload.py`: Uploads CSV to S3
- `emr_data_processing.py`: Processes CSV using PySpark
- `redshift_integration.py`: Loads processed data into Redshift

## Prerequisites
- AWS account with S3, EMR, and Redshift access
- AWS credentials set via environment or config
- Python 3.x

## How to Run
1. Upload data to S3:
```bash
python s3_upload.py
