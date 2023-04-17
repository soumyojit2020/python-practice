"""
Python script to query a MySQL db and put the extract into a GCP bucket
- take a file that contains an SQL query
- execute it against a MySQL instance
- export the response into a CSV file
- push the CSV file into GCP bucket
"""

import mysql.connector
from google.cloud import storage
from datetime import datetime

# MySQL connection information
mysql_host = 'HOSTNAME'
mysql_user = 'USERNAME'
mysql_password = 'PASSWORD'
mysql_database = 'DATABASE'

# GCP information
gcp_project_id = 'PROJECT_ID'
gcp_bucket_name = 'BUCKET_NAME'
gcp_credentials_file = 'PATH_TO_CREDENTIALS_FILE'

# SQL query file
sql_query_file = 'PATH_TO_SQL_FILE'

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# Read SQL query from file
with open(sql_query_file, 'r') as file:
    sql_query = file.read()

# Execute SQL query
cursor = mysql_conn.cursor()
cursor.execute(sql_query)
result = cursor.fetchall()

# Export result to CSV file
filename_prefix = 'configurable-identifier'
timestamp = datetime.now().strftime('%y-%m-%dT%H:%M:%S')
filename = f'{filename_prefix}-{timestamp}.csv'
with open(filename, 'w') as file:
    for row in result:
        file.write(','.join(str(x) for x in row) + '\n')

# Upload file to GCP bucket
storage_client = storage.Client.from_service_account_json(gcp_credentials_file, project=gcp_project_id)
bucket = storage_client.bucket(gcp_bucket_name)
blob = bucket.blob(filename)
blob.upload_from_filename(filename)
