from faker import Faker
import pika

import connect
from models import User


faker = Faker()


credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue="send_email")

for _ in range(10):
    
    user = User(
        fullname=faker.name(),
        email=faker.email(),
        phone_number=faker.phone_number()
    ).save()

    channel.basic_publish(exchange="", 
                          routing_key="send_email", 
                          body=str(user.id))