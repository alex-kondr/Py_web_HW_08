import pika

import connect
from models import User


def send_email(*args):
    
    _id = args[3].decode()
    
    user = User.objects(id=_id)
    user.update(message_sent=True)
    
    print(f"Sended message by {user[0].fullname}")
    
    
credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue="send_email")

channel.basic_consume(queue="send_email", on_message_callback=send_email, auto_ack=True)

channel.start_consuming()
connection.close()