##  Step 1
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

## step 2.5
the next step was or half step was to extract the data I was ooking for so I replicated the initial process of printing the data and calling the key names of the  values I need.
 
![pokedex step 2 5 extra data](https://github.com/user-attachments/assets/3feb9e5c-2b26-4e63-8f6d-6b5d49eed4fe)

---


 ## step 2.75
 the next little issue was concerning a nested value within the api, I defintely needed to brush up on my handling of dictionaires and  accessing indices.

 ![pokedex step 2 75 nested keys](https://github.com/user-attachments/assets/8350afe7-45d6-497d-a9b4-b8abcc8bd052)
 

yeaaaah so I brushed up on accessing dictionary indices and went a little buck wild and added move sets for each pokemon as well! So currently I'm just printing out the values for each key I'm calling, that's definitely not how things will be. This was more to see how the data was looking for each pokemon, what should happen next on my end would be creating a variable for each of the data points called and from there I'll create a for- loop and loop all the data into a dictionary and voilà!  But that's what step 3 is for!

![pokedex step 2 95](https://github.com/user-attachments/assets/f409464d-b992-44ba-9bbe-640253daf593)

---


## step 3
Step tres (3); So this step will be the step where I plan to create variables and take the values within each variable and place them into a dictionary by creating a for-loop. That's the plan as of right now, lets see how it actually goes!

Hey! I'm back, So defintely easier said than done but here was the process:

1) I had the scraped data printed within the for-loop and not saved to any variable, whoch would make it difficult for the later conversion into a dictionary so that was prioroity number one.

![pokedex step 3 1](https://github.com/user-attachments/assets/03b274bc-1d7d-4824-bd38-1ea0a5552de8)

2) I then had to create lists outside of the function (that corresponded to the lists within the for-loop) where I would append the scraped data that had just been placed within a list.

![pokedex step 3 2](https://github.com/user-attachments/assets/378b5dfc-dcbe-4c2a-ae3a-d97c09450ceb)   

![pokedex step 3 25](https://github.com/user-attachments/assets/9172bf87-391a-4d86-b45d-0b770313b3d5)

3) Once all the lists were appended; I had to take the lists, zip them into a variable called pokemon_data and create a dict comprehension called pokemon_dict ( easier said than done, I had to get a little refresher on how to handle dictionaries)
   - I was initially unsure if I could zip more than 2 lists together (the most I'd done in the past was 2). I also was unsure of i could create a singular dict comprehension for all these lists or if it was something I had to do a few times over. so I had to do a bit of reading and practice on a virtual environment through codecademy, and eventually I figured out how to create a key: value(s) pair and below is the result:

![pokedex step 3 3](https://github.com/user-attachments/assets/929e6536-c2b6-4532-b94f-3974c73af0df)

output:

![pokedex step 3 3 output](https://github.com/user-attachments/assets/b5d81a80-0786-47f7-979c-c4a31aaa8d07)

---

## step 4
step 4!!! the finish line's within reach!! (hopefully 👀)
last step should be easy work, all I have to do is use the pandas DataFrame() function on the dictionary and game over right?

No. 🥲

So I did use the pandas Dataframe function on the pokemon_dict and named the dataframe pokedex_df. I thought that meant game over but decided to print out the dataframe just to make sure and this was what I got:

![pokedex step 4 og dataframe](https://github.com/user-attachments/assets/aaeb3278-0300-4883-8e62-62c5e4ca78f4)

It's definitely a dataframe, but not what I had envisioned it to be. Rather than the pokemon ID's as the columns, I had envisioned the dataframe to display each pokemon's information in rows across the table and for the columns to be names that represents clearly the data under each column. In order for me to do that I used the .transpose() function on the pokemon_df.
The .transpose() function is a function within the pandas library that flips a table by swapping the matrices ( columns and rows) with eachother wich would give me my desired result:

Here's the code:

![pokedex step 4 transpose](https://github.com/user-attachments/assets/0a6b8492-0800-452f-993a-96552c54427d)

The result:

![pokedex step 4 transpose result](https://github.com/user-attachments/assets/58ddacf9-49b4-495a-b8e1-8bc37c4c8b32)

Done right? No

The next item on the docket was finding out a way to rename the columns so that each of the data types extracted could be labled accordlingly, so I created a list of the column names called; dfcolumn_names.
I set pokedex_table.columns = dfcolumn_names, to replace the original column names, this is the code:

![pokedex step 4 column rename](https://github.com/user-attachments/assets/89b86350-f0d4-454c-98ae-0a5898b9bcb9)

Here is the result:

![pokedex step 4 column rename output](https://github.com/user-attachments/assets/0be67962-65f3-4064-adb1-38d30a4353d3)

---
## step 5 😪
this step I just cleanup really, there are a few things i wanted to change:
 - so the height of the pokemon were recorded in decimeters, why I don't know, so I looked up the conversion rate of decimeters to centimeters and found that I'd have to multply the provided values by 10 to convert it to centimeters. I did this by performing a function on the 'height' column of the dataframe and multiplied the entire column by 10.
 - Similarly to height, weight was also recorded in hectograms, why I don't know 😅, so found the conversion rate between hectograms and kilograms, the conversion would have me divide the column by 10 for the values to be converted to kilos. I then performed a function on the 'weight' column and just like magic; Kilograms.
 - I then changed the column headers accordingly to 'height(cm)' and 'weight(kg)'

here's the code below:

![pokedex step 5 cleanup](https://github.com/user-attachments/assets/b7d1a40a-0722-4e91-9e9c-ae8bc54c1ba7)


here's the output:

![pokedex step 5 clean up results](https://github.com/user-attachments/assets/62d737fa-55ab-487e-bf58-e64c01465874)

- Last but not least I wanted all  the pokemon names to be in title case, so i used the pandas .str.title() function on the 'name' column.
here's the code:

![pokedex step 5 case](https://github.com/user-attachments/assets/9fd500eb-427f-4561-9c0e-7d6f33eee3f7)


here's the output:

![pokedex step 5 case output](https://github.com/user-attachments/assets/0fc082cb-116e-4fc2-8341-dac8325e1674)

---

## Final Thoughts and Reflections
It feels good to complete my first completely unguided python project 🎉! I initially saw it as a daunting task, one that I honestly didnt know if I'd be able to complete atleast in the timeframe I had given myself. As I continued on through the project and each obstacle set in front was overcome, the task became less and less intimidating and I began to tackle situation with curiosity and optimism. This project was a solid way for me to practice working with an API and organizing real-world data using Python. My goal was to scrape key details from the PokeAPI — things like name, type, moves, height, and weight — and present it all in a clean and readable format. What I absolutely enjoyed most about the process was seeing everything come together — going from raw data to a full table that actually made sense and could be analyzed or built on later. Overall, it gave me a stronger understanding of how to collect and structure data in a way that makes it easier to work with.










 
