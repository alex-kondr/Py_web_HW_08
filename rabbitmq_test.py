import pika

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters("localhost", 49154, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()