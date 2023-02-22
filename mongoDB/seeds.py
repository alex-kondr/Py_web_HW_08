import json
from pathlib import Path

import connect
from models import Author, Quote


path = Path(__file__).parent


def load_json_file(file: str):    

    with open(path.joinpath(file), "r") as fd:
        return json.load(fd)   


if __name__ == "__main__":
    
    authors = load_json_file("authors.json") 
    
    [Author(**author).save() for author in authors]        
        
    quotes = load_json_file("quotes.json")
    
    for quote in quotes:        
        
        qoute_author = quote.get("author")        
        author_obj = Author.objects(fullname=qoute_author).first()      
        quote["author"] = author_obj
        
        Quote(**quote).save()
    