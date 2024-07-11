import json
from google.cloud import tasks_v2
from google.cloud.tasks_v2.services.cloud_tasks.transports import CloudTasksGrpcTransport


def main_f1(request):
    print(f"Received request: {request}")

    # Create a topic.
    topic = "projects/testproj/topics/topic-a"
    pubsub_attributes = {
        "key": "value"
    }

    # Create json data for testing pubsub message
    json_data = {
        "status": "salutations",
        "data": "payload data here..."
    }
    json_encoded = json.dumps(json_data).encode('utf-8')

    task_json = {
        "http_request": {
            "http_method": self.http_method,
            "url": self.url,
            "body": None,
            "headers": {"Content-Type": "application/json"}
        }
    }

    channel = grpc.insecure_channel("127.0.0.1:8123")
    transport = CloudTasksGrpcTransport(channel=channel)
    task_mgr = tasks_v2.CloudTasksClient(transport=transport)
    parent = task_mgr.queue_path("testproj", "us-central1", "queue-a")
    task = task_mgr.create_task(parent=parent, task=task_json)
    print("task created successfully! {task}")    


   # Create a Publisher client.
    # publisher = pubsub_v1.PublisherClient()

    # # Publish a message to the topic.
    # future = publisher.publish(topic=topic, data=json_encoded, **pubsub_attributes)
    # if future.exception(timeout=30):
    #     print(future.exception())
    # else:
    #     print("published successfully!")
    #     print(future.result())

    return "OK"
