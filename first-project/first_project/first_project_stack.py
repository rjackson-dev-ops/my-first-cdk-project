from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as _s3,
    RemovalPolicy as _removal_policy
)
from constructs import Construct

class FirstProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self, "MyFirstBucket",
            versioned=True,
            bucket_name="myfirstbucket-12-29-2021",
            encryption=_s3.BucketEncryption.KMS_MANAGED,
            removal_policy=_removal_policy.DESTROY
        )