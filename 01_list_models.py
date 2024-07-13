# Use the ListFoundationModels API to show the models that are available in &BR; in a given region.
import boto3
             
# Create an &BR; client in the &region-us-east-1; Region.
bedrock = boto3.client(
    service_name="bedrock",
    region_name="us-east-1"
)

print(bedrock.list_foundation_models())