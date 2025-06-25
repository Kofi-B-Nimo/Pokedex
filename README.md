# Pokedex
Creating my own small pokedex of a few Pokémon using python!

## Project Overview
This project uses Python to retrieve data on Pokémon from the PokéAPI. Key attributes like name, height, weight, and type are extracted and organized into a Pandas DataFrame for easy analysis and exploration.

---

## Step 1
To begin the project, my initial steps involve taking a look at the PokeAPI, and getting insight of how exactly the data's structured in order for me to understand how to go about scraping the website. after checking out the website, I can say the data is formatted using key-value pairs (JSON formatting).

![PokeAPI formatting](https://github.com/user-attachments/assets/fc621132-24ed-44cd-a2ab-0e4718b317fd)

---

## Step 2
the next step involves using the Requests library in Python to extract the necessary data from the PokeAPI, which includes pokemon number, name, type,height, weight, location, and etc. I should be able to achieve this by creating a for-loop and iterrating through the desired number of pokemon (using each pokemon's ID number) to extract the data I'm looking for. 

so......
I had to slow my role a bit and not try and extract all that data at once. I focused first on just making sure i could extract the names of the pokemon based on their ID numbers.
So step 2 consists of creating a function that would:
- initiate a for-loop that loops through the pokemon id numbers
- while looping through the pokemon id's, each time the request status is checked
- if the request status is a success; the function returns the name of each pokemon within the range provided 

here's a screenshot of what that looks like and the output return for step 2

code:

![pokedex py step 1](https://github.com/user-attachments/assets/799ed154-6c7d-4e2a-ba91-2ff9399e47a9)

output:

![pokedex py step 1 output](https://github.com/user-attachments/assets/7f716cba-f455-46fa-b84c-efd6e6c1c859)

---

## Step 3
this step will consist of retrieving all the info wanted from the API and placing the data into a dictionary.
The dictionary; 'pokemon_dict' was created to, for now, to house all the scraped data and this is a brief outline of the process:
- Create empty lists outside the function and name them corresponding to the requested data within the for-loop
- Take all the the requested data being printed within the for-loop and assign the data to variables
- Then append the data within the for-loop to the lists outside the for-loop (so that everytime an iteration cycle is complete all the requested information for each pokemon is added)
- Once all the necesarry data has been appended to the lists, a variable called pokemon_data was created that contained a zip of all 8 lists (poke_ids, pokemon_names, types, moves1, moves2, moves3, heights, weights)
- In order to create a dictionary a dict comprehension was utilized by assigning poke_ids as the key and the remaining 7 lists and the values
- The created dictionary was called pokemon_dict

appending data into lists:

![pokedex step 3 README md lists](https://github.com/user-attachments/assets/c2c0d4c8-ee86-45ee-942e-59c01640bdae)

zipped list into a dictionary:

![pokedex step 3 README md dicts](https://github.com/user-attachments/assets/b58644e0-c014-49d5-9399-58c8b2f5a04c)

dictionary output:

![pokedex step 3 3 output](https://github.com/user-attachments/assets/c52f0fe6-2f2b-4aeb-80fe-cf12e634d577)

---

## Step 4 
- Created a DataFrame from pokemon_dict using pd.DataFrame() and named it pokedex_df.
- Upon inspecting the DataFrame, the layout wasn’t what I expected — Pokémon IDs became columns instead of rows.
- Used .transpose() to flip the DataFrame so that each Pokémon became a row and the data types (like name, type, height, etc.) became columns.
- This successfully flipped the table to match the structure I envisioned.
- Next, I created a list called dfcolumn_names to manually assign readable column headers.
- Used pokedex_table.columns = dfcolumn_names to rename the columns to match the data under them.
- The result: a well-structured, clean DataFrame with Pokémon data organized row by row and labeled clearly.

Dataframe transpose:

![pokedex step 4 transpose](https://github.com/user-attachments/assets/1024ce6c-201b-4d63-b6c0-61594ddd4d38)

transpose  of the dataframe result:

![pokedex step 4 transpose result](https://github.com/user-attachments/assets/5dcc32a0-021a-4135-8f3e-90e054dfa95e)

column rename results:

![pokedex step 4 column rename output](https://github.com/user-attachments/assets/528e2729-bc55-4d68-89dc-a24f7ba5aa29)




---

##  `Step 5 `

- Wanted to tidy up a few final details to make the DataFrame cleaner and easier to understand.

- 📏 **Height conversion:**
  - The API gave height values in **decimeters** (why? I don’t know 🤷🏾‍♂️).
  - I looked up the conversion rate — multiplying by `10` gave me centimeters.
  - Applied the change directly to the `'height'` column.









