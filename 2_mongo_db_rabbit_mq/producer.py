from random import choice

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
channel.queue_declare(queue="send_sms")

for _ in range(10):
    
    user = User(
        fullname=faker.name(),
        email=faker.email(),
        phone_number=faker.phone_number(),
        preferred_communication=choice(("SMS", "email"))
    ).save()

    match str(user.preferred_communication):
        
        case "SMS":
            channel.basic_publish(exchange="", 
                                routing_key="send_sms", 
                                body=str(user.id))
            
        case "email":
            channel.basic_publish(exchange="", 
                                routing_key="send_email", 
                                body=str(user.id))