from flask import Flask,render_template,request
from jikan import getidbyname,get_common_anime,get_anime_details,getAnimeStreamingService



app = Flask(__name__) #configure application

if __name__ == "__main__":
    app.run(debug=True)  #devlopers options enabled


@app.route("/", methods = ["GET","POST"])
def home():
    """homepage to enter titles"""
    if request.method == "POST":
        anime_names = []
        anime_ids = []
        #extract the data from the input box 
        for i in range(len(request.form.getlist('anime[]'))):
            anime_name = request.form.getlist('anime[]')[i]
            if anime_name:
                anime_names.append(anime_name)
        
        #doing the api call to get the anime ids
        for anime_name in anime_names:
            anime_id = getidbyname(query=anime_name)
            
            if anime_id:
                anime_ids.append(anime_id)
        #getting the recomendation list (mal_ids list)
        final_recomendation = get_common_anime(anime_ids)
        if final_recomendation:
            detailed_recomendation = []
            for anime in final_recomendation:
                full_info = get_anime_details(anime)
                if full_info:
                    detailed_recomendation.append(full_info)
            if detailed_recomendation:    
                return render_template("recom.html",recommendations = detailed_recomendation)
        else:
            return "No valid recommendations found", 404

    else:
        return render_template("home.html")


@app.route("/streaming/<int:anime_id>/<string:anime_title>/<path:anime_img>")
def streaming_options(anime_id,anime_title,anime_img):  # This function name should match the one used in url_for()
    # Here you would typically fetch the streaming options for the given anime_id
    # For now, we'll just pass the anime_id to the template

    data = getAnimeStreamingService(anime_id)

    

    return render_template("stream.html",
                             anime_id=anime_id,
                             anime_title=anime_title,
                             anime_img=anime_img,
                             streaming_options=data
                            )
