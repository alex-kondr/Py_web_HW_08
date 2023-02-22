import pika



def process_message(channel, method, properties, body):
    
    print(f"Channel: {channel}")
    print(f"Method: {method}")
    print(f"Properties: {properties}")
    print(f"Body: {body}")



credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue="test")

channel.basic_consume(queue="test", on_message_callback=process_message, auto_ack=True)

channel.start_consuming()
connection.close()

# acknowledged