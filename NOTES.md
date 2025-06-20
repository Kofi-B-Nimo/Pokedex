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
Step tres (three); So this step will be the step where 




 
