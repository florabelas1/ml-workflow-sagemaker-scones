#classifier
import json
import base64
import boto3

ENDPOINT = "image-classification-2025-09-19-19-15-12-655"

runtime = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):


    image_data = base64.b64decode(event["image_data"])



    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",
        Body=image_data
    )


    inferences = response["Body"].read()    
    


    event["inferences"] = inferences.decode("utf-8")  

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }



#filterLowConfidence

import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    
    inferences_str = event["inferences"]
    inferences = json.loads(inferences_str)   

    meets_threshold = max(inferences) >= THRESHOLD

    if not meets_threshold:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return event

#serializeImageData
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    key = event["s3_key"]
    bucket = event["s3_bucket"]

    # Download image from S3 para /tmp
    s3.download_file(bucket, key, "/tmp/image.png")

    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
