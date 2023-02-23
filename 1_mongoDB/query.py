import redis
from redis_lru import RedisLRU

import connect
from models import Author, Quote


client_redis = redis.Redis(host="127.0.0.1", port=6379)
cache = RedisLRU(client_redis)


def handler(command):

    try:
        key, value = command.split(": ")
        
        match key:
            case "name":
                return get_quotes_by_author(value)
            
            case "tag":
                return get_quotes_by_tag(value)
            
            case "tags":
                return get_quotes_by_tags(value)
                
            case _:
                return "No such this command"
                
        # commands = {
        #     "name": get_quotes_by_author,
        #     "tag": get_quotes_by_tag,
        #     "tags": get_quotes_by_tags
        # }
        
        # result = commands[key](value)
        
        # return result
        
    except ValueError as err:
        print(err)


def quotes_obj_to_list(quotes):
    return [quote.quote for quote in quotes]


@cache     
def get_quotes_by_author(name: str) -> list[str]:
    
    author = (Author.objects(fullname=name).first() or
        Author.objects(fullname={"$regex": "^"+name, "$options": "i"}).first())
        
    quotes = Quote.objects(author=author)
    
    return quotes_obj_to_list(quotes)


@cache
def get_quotes_by_tag(tag: str) -> list[str]:
    
    quotes = (Quote.objects(tags=tag) or
        Quote.objects(tags={"$regex": "^"+tag, "$options": "i"}))
    
    return quotes_obj_to_list(quotes)


def get_quotes_by_tags(tags: str) -> list[str]:
    
    quotes = Quote.objects(tags__in=[tag for tag in tags.split(",")])
    
    return quotes_obj_to_list(quotes)


if __name__ == "__main__":
    
    while True:
        
        command = input("input key: value \n")
        
        if command == "exit":
            break
        
        result = handler(command)
        
        print(result)