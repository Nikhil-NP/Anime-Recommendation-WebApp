import requests #To fetch jikan API calls
from collections import Counter #this will get me the common elements amoung list 


def getidbyname(query):
    """
    This takes in query(anime_name) tries to return the mal_id(MYANIMELIST) using Jikan v4 API
    i have modified it to only return mal_id when the type : 'TV'

    Args:
         str : takes in a string aka anime title

    Return:
        int : try to  gives out the anime_id of the anime 

    """
    
    try:
        serach_url = f"https://api.jikan.moe/v4/anime?q={query}"
        search_responce = requests.get(serach_url).json()
        i = 0
        n = 10#this is total random number i felt the best would be to see the top 
        for i in range(n):#making sure i am getting the mal of the anime not the movie with the title 
            if search_responce['data'][i]['type'] == 'TV':
                mal_id = search_responce['data'][i]['mal_id']
                return mal_id
        return None
    except requests.exceptions.RequestException as e :#if anime doesnt exist
        print(f"exception occured : {e}")
        return None
    except KeyError as e:
        print(f"error while fetching the anime {e}")
        return None
def recomendation_list(id):
    """
    This will take in a anime_mal_id and give our the mal_id of all the anime that 
    are recommended by it 
    this will be used in jikan.py itself not in app.py
    Args:
        int: it takes in MAL_ID of anime titles

    Return:
        list : a list that contains all MAL_IDs of all the similar order in most>least similar ascending order

    """
    try:
        recomendations_url = f"https://api.jikan.moe/v4/anime/{id}/recommendations"
        recomendation_responce = requests.get(recomendations_url).json()             #{[{     }]} this will get raw json
        titles = recomendation_responce['data']#geting the specific data
        recomendation = []
        for i,title in enumerate(titles):#extracting the mal for all the titles
            recomendation.append(title['entry']['mal_id'])
        return recomendation
    except requests.exceptions.RequestException as e :#if anime doesnt exist
        print(f"exception occured : {e}")
        return None
    except KeyError as e:
        print(f"error while fetching the anime {e}")
        return None
    
def get_common_anime(anime_ids,top_N=5):
    """
    this will generate the top 5 anime recomendation that best suits users taste 


    Args:
        Takes in 2 args, 1 :the list contaning all the anime ids that user wants us to conider,the top_n number of anime we will omit 

    return :
        this will return a list of  Max: top 5 anime ids  based on common amoung all the anime

    """
    all_animes = []
    for anime_id in anime_ids:#this will create a mega list of all the anime recomendations ofcourese many titles will be repeated 
        recomendations = recomendation_list(anime_id)
        if recomendations:#making sure if the title is not same as input from user
            all_animes.extend(recomendations)
    
    common_animes_id = Counter(all_animes)#this will create a hashmap count all the ids with the no of time they are repeated 
    most_common_anime = sorted(common_animes_id.items(),key=lambda columb:(-columb[1]))#-columb[1] the list in discending order with most common 
    
    return [recomendation[0] for recomendation in most_common_anime[:top_N] ]




def get_anime_details(anime_id):
    """
    Fetch general info about each anime from jikan api 

    Args:
        int contining the mal id of the anime 

    Return:
        return a dict of anime basic information 
    """
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    raw_data = requests.get(url)
    if raw_data.status_code == 200:
        detials = raw_data.json()['data']
        return{#data to render in the recom.html 
            'id' : anime_id,
            'title' : detials['title_english'],
            'synopsis' : detials['synopsis'],
            'img' : detials['images']['jpg']['image_url'],
            'episodes' : detials['episodes'],
            'status' : detials['status'],
            'score' : detials['score']
        }
    else:
        print(f"error fetching details for anime having id : {anime_id} status code : {raw_data.status_code}")
        return None
    

def getAnimeStreamingService(anime_id):
    """
        Fetch streaming services

        Args:
            int contining the mal id of the anime 

        Return:
            return a list  of anime 

    """
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/streaming"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and isinstance(data['data'], list):
            # Create the dictionary comprehension only if 'data' is a list
            streaming_sites = {item['name']: item['url'] for item in data['data'] if 'name' in item and 'url' in item}
            return streaming_sites

        else:
            print("Unexpected data structure in the API response")
            return None
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None


