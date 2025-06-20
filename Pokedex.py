import requests
import pandas as pd

# import the requests library to retrieve the website and scrape the info needed
# import pandas to take the extracted data and turn it into a pandas DataFrame


url = 'https://pokeapi.co/api/v2/'
# saving the url of the website in a variable to be used in a function

# catch = requests.get(url)
# print(catch)
# was checking to see if the request was successful, came backa s 200

def pokedex():
    # pokemon_url = f'{url}/pokemon/{id}'
    # catch = requests.get(pokemon_url)
    
    for poke_id in range (1,21):
        pokemon_url = f'{url}/pokemon/{poke_id}'
        catch = requests.get(pokemon_url)
        
        if catch.status_code == 200:
            data = catch.json()
        
        print(data['id'])
        print(data['name'])
        print(data['types'][0]['type']['name'])
        print(data['moves'][0]['move']['name'])
        print(data['moves'][1]['move']['name'])
        print(data['moves'][2]['move']['name'])
        print(data['height'])
        print(data['weight'])
        
        
        # print(data.keys())
         
# the pokedex function has a for loop within it that iteerates through the first 20 pokemon based on their ID number.
# I used the f string in the pokemon_url so that the pokemon id number within the url was mutable
# got the status code of the request to make sure that the data extraction was a success and if it was succesful, the data 
# would then be returned in a readable format using .json(), so for now we called for only the pokemon names to get printed
# based on their id numbers
   
    
    
pokedex()


    
    
