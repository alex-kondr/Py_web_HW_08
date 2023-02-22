import redis


client = redis.Redis(host="127.0.0.1", port=6379)
client.set("key12", "value1123")
# print(type(client.get("key").decode()))