import requests
from random import randint

def get_random_sentence():
    url = "https://dummyjson.com/quotes"


    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        
        index = randint(0,30)
        
        sentence = data['quotes'][index]['quote']
        
        return sentence


    except requests.RequestException:
        print("\nUnable to connect to sentence API.")
        return None



