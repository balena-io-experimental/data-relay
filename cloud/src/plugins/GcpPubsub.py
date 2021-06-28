import os

NAME = "GCP Pubsub"
TYPE = "remote"
FILE = "GcpPubsub.yaml"
VARS = [
    "GCP_PUBSUB_TOPIC",
    "GCP_PUBSUB_SUBSCRIPTION",
    "GCP_PUBSUB_TYPE",
    "GCP_PUBSUB_PROJECT_ID",
    "GCP_PUBSUB_CLIENT_EMAIL",
    "GCP_PUBSUB_PRIVATE_KEY"
]

def invoke():
    if os.getenv("GCP_PUBSUB_SUBSCRIPTION") is None:
        print("Setting GCP Pub/Sub subscription to the default: unknown")
        os.environ["GCP_PUBSUB_SUBSCRIPTION"] = "unknown"
