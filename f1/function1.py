from google.cloud import pubsub_v1

def function1(request):
    print(f"Received request: {request}")
    # Create a Publisher client.
    publisher = pubsub_v1.PublisherClient()

    # Create a topic.
    topic_path = publisher.topic_path('my-project', 'my-topic')
    topic = publisher.create_topic(topic_path)

    # Publish a message.
    data = b'Hello, World!'
    future = publisher.publish(topic=topic_path, data=data)
    print(f"Published {data} to {topic_path}.")
    
    if future.exception(timeout=30):
        print(future.exception())
    else:
        print(future.result())