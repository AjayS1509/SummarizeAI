from flask import render_template, request, jsonify
from modules import modules, validUrl

def configure_routes(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        return render_template("index.html", hello=hello, content=content)
    
    @app.route("/api/yturl", methods=["POST"])
    def yturl():
        
        try:
            # Extract the JSON data from the request
            data = request.get_json()
        
            # Ensure 'url' key is present in the JSON payload
            if not data or "url" not in data:
                return jsonify({"error": "No URL provided"}), 400
        
            # Get the YouTube URL
            youtube_url = data["url"]

            if(validUrl.is_valid_youtube_url(youtube_url)):


                #print(youtube_url)

                # try:
                #     modules.yt_audio_extractor(youtube_url)

                # except  Exception as e:
                #     return jsonify({"error coverting audio": str(e)}), 500

                try:
                    yt_text = modules.yt_transcript_api(youtube_url)
                    #print(yt_text)
                    return jsonify({"message": "URL received successfully","a_yt_url":youtube_url, "transcript": yt_text}), 200
                    
                
                except:
                    return jsonify({"error coverting text": str(e)}), 500
                
                # # Process the YouTube URL (you can add validation or other processing here)
                # if "youtube.com" not in youtube_url and "youtu.be" not in youtube_url:
                #    return jsonify({"error": "Invalid YouTube URL"}), 400

                # # Respond with success
                # return jsonify({"message": "URL received successfully", "url": youtube_url}), 200
            else :
                return jsonify({"error in url": str(e)}), 500

        except Exception as e:
            return jsonify({"error": str(e)}), 500
