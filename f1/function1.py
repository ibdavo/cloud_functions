from google.cloud import pubsub_v1
import json 

def main_f1(request):
    print(f"Received request: {request}")
 
    # Create a topic.
    topic = "projects/testproj/topics/topic-a"
    pubsub_attributes = {
                "key": "value"
            }
    
    # Create json data for testing pubsub message
    json_data = {
        "message" : "hello world",
        "status" : "salutations",
        "data" : "payload data here..."
    }
    json_encoded = json.dumps(json_data).encode('utf-8')

   # Create a Publisher client.
    publisher = pubsub_v1.PublisherClient()

    # Publish a message to the topic.
    # future = publisher.publish(topic=topic, data=json_encoded)
    future = publisher.publish(topic=topic, data=json_encoded, **pubsub_attributes)
    # future = pubsub_client.publish(topic=topic, data=json_str, **pubsub_attributes)
    # future = pubsub_client.publish(topic=topic, data=json_str)    
    if future.exception(timeout=30):
        print(future.exception())
    else:
        print("published successfully!")
        print(future.result())

    return "OK"
    