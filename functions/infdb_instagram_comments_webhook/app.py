import boto3
from botocore.exceptions import ClientError
import logging
from datetime import datetime
import json
import requests
import csv

# boto3 S3 initialization
s3_client = boto3.client('s3')


def lambda_handler(event, context):

    event_obj = json.loads(json.dumps(event))

    data = json.loads(event_obj['body'])

    current_date = datetime.today().strftime('%Y-%m-%d')

    # if there is no new posts, data comes as None
    if data['resultObject'] is not None:

        download = requests.get(
            "https://docs.google.com/spreadsheet/ccc?key=1AHy_iqUlDdd7NOh20PyU5vutMnKTLIn_y95JKW2hyig&output=csv")

        decoded_content = download.content.decode('utf-8')

        cr = csv.DictReader(decoded_content.splitlines(), delimiter=',')

        for row in cr:
            if row['postUrl'] == json.loads(data['resultObject'])[0]['query']:
                object_name = "raw_files/{0}/{1}.json".format(row['username'], current_date)
            else:
                object_name = ""

        bucket_name = 'infdb-data-store-dev'

        file_url = "https://phantombuster.s3.amazonaws.com/7lwPTCxbhH8/zDCVZvofS135Ke3mlHcJ4Q/result.json"

        file_data = requests.get(file_url).json()

        file_path = '/tmp/' + "{0}-raw.json".format(file_data[0]['username'])

        with open(file_path, 'w') as f:

            json.dump(file_data, f, ensure_ascii=False, indent=4)

        try:
            response = s3_client.upload_file(file_path, bucket_name, object_name)

        except ClientError as e:
            logging.error(e)
            return False

    else:
        print("No new post found.")

    return {
        'statusCode': 200
    }
