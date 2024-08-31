# Anime Recommendation System

date:31/08/2024
by Nikhil Purohit,India
my github account: https://github.com/Nikhil-NP
Edx account username : nikh09
github link:https://github.com/Nikhil-NP/Anime-Recommendation-System


### Video Demo: https://youtu.be/5U3z5quXlsk


An Anime Recommendation System that allows users to input anime names, get suggestions based on their input, select a suggestion, and choose a streaming platform to be redirected to its website.

## Features

- Input single/mutliple anime name to get recommendations.
- Get suggestions based on the entered anime's,uses's counter from collection to find most common recommended title amoung the recommemded titles .
- Select a suggestion to view details.
- Redirect to streaming platforms for watching.

## Walthrough each file
### main.py 
- this has the core logic of my project ,its the connecting part where jinja/html/css(frontend) communicate with the backend jikan.py 
### jikan.py
- this has all the functions of the code basically all the api calls , manipulation of json takes place here and i have also used collections table to find common titles amoung the recommended set of animes

### templates 
- it has all the html front end like the layout.html the base template
- home.html is the index page where you land when you enter the site 
- recom.html is where you are redirected when you press enter after typing of anime names
- stream.html is where to go to see al the avilabe streaming options 

### static
- to ensure the website looks asthetically pleasing made some design and color choices

### .gitignore 
-these were some ruff draft conept idea early on while building this which i still keep as reference



## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Nikhil-NP/Anime-Recommendation-system

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   