import connect
from models import Author, Quote


def handler(command):

    try:
        key, value = command.split(": ")    
                
        commands = {
            "name": get_quotes_by_author,
            "tag": get_quotes_by_tag,
            "tags": get_quotes_by_tags
        }
        
        result = commands[key](value)
        
        return result
        
    except ValueError as err:
        print(err)
        
        
def get_quotes_by_author(name: str) -> list[str]:
    
    author = Author.objects(fullname=name).first()
    quotes = Quote.objects(author=author)
    
    return [quote.quote for quote in quotes]


def get_quotes_by_tag(tag: str) -> list[str]:
    
    quotes = Quote.objects(tags=tag)
    
    return [quote.quote for quote in quotes]


def get_quotes_by_tags(tags: str) -> list[str]:
    
    quotes = Quote.objects(tags__in=[tag for tag in tags.split(",")])
    
    return [quote.quote for quote in quotes]


if __name__ == "__main__":
    
    while True:
        
        command = input("input key: value \n")
        
        if command == "exit":
            break
        
        result = handler(command)
        
        print(result)