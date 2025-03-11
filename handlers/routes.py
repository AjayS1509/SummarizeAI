from flask import render_template, request, jsonify
from modules import modules, validUrl, download , whisper_summary, summarize, upload, getFile
import whisper
import torch
import warnings
import os

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



    @app.route("/api/yt_multi_lang", methods=["POST"])
    def yt_multi_lang():

        try:
            # Extract the JSON data from the request
            data = request.get_json()

            if not data or "url" not in data:
                return jsonify({"error": "No URL provided"}), 400
            

            youtube_url = data["url"]
            language = data.get("language", "English")  # Defaults to English if 'language' is missing


            try:

                video_URL = str(youtube_url)
                destination = "./audio_files"
                final_filename = "speech1"
                download.download_mp3(video_URL, destination, final_filename)

                #res = whisper_summary.whisper()
                summary = ""
                
                try:
                    # Suppress FutureWarnings related to torch.load
                    warnings.simplefilter("ignore", category=FutureWarning)

                    # Set device
                    device = "cuda" if torch.cuda.is_available() else "cpu"

                    # Load Whisper model
                    whisper_model = whisper.load_model("base", device=device)

                    # Transcribe audio
                    audio_file = "./audio_files/speech1.mp3"
                    res = whisper_model.transcribe(audio_file)
                    text_data = res["text"]
                    #result_ADO = 
                    print("done text")
                    #print("transcript done", text_data)
                    try:
                        
                        summary = summarize.abstractive_summarization(text_data, language)

                    except:
                        print("Error 4+")

                
                except:
                    print("Error 3+")
                    summary = ""
                
                return jsonify({"message": "URL received successfully","a_yt_url":youtube_url, "transcript": text_data, "summary": summary}), 200

                # try:
                #    


                # except:
                #      return jsonify({"error": str(e)}), 500



            except:
                print("Error 1+")

                return jsonify({"error": str(e)}), 500
        

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        




    @app.route("/api/temp_data", methods=["POST"])
    def temp_data():
        #data = '<strong>Summary of Video Explanation</strong><br><strong>Heading:</strong><br>"Python classes are like blueprints for creating objects. They define the attributes, methods, and behavior of each object. By initializing objects with specific attributes and defining additional methods, you can create unique objects that interact with the environment in specific ways."<br>---<br><strong>Key Points:</strong><br><strong>1. Attributes as Blueprint: Python classes act like blueprints, specifying essential attributes (e.g., health, damage, speed) for creating objects.</strong><br><strong>2. Dynamic Initialization: When an object is created from a class, its __init__ method initializes it with the specified attributes and methods are defined to create new objects when methods are called.</strong><br><strong>3. Self Variable: The self variable is automatically placed at the first position in each object, allowing you to reference the current object. You don't need to explicitly call `self` (e.g., `self.speed`), but it's conventional practice.</strong><br><strong>4. Adding Methods for Behavior: By defining methods on a class, you can customize how objects act with their environment. For example, adding a method called `double_speed` that modifies the object's speed attribute.</strong><br><strong>5. Unique Objects: Each object created from a different class or subclass is unique and has its own attributes and behaviors, making your code more maintainable and flexible.</strong><br>
        data = "<strong>Subheading:</strong><br><strong>Python Classes as Blueprints for Objects</strong><br><strong>Points:</strong><br><strong>1. __init__: A Default Method for Object Creation: When you create a Python class object (e.g., ` Warrior` or `Ninja`), the __init__ method runs first, initializing the object with attributes like health, damage, and speed. This ensures that each instance has its own set of properties defined at initialization.</strong><br><strong>2. Handling Inputs Through __init__: The Typical Naming Convention: You do not need to explicitly name parameters in __init__, but it is conventional to place them as the first argument when defining a class. For example, `self` is used implicitly, and attributes are named conventions like `health`, `damage`, or `speed`.</strong><br><strong>3. Typical Input Handling: The __init__ method can automatically handle inputs through its parameters. If you provide values for certain attributes during object creation, those values take precedence over the defaults. For example:</strong><br>- `Warrior`: `health=100`, `damage=50`<br>- `Ninja`: `health=80`, `damage=40`<br><strong>4. Adding Functionality to Classes: After defining a class with attributes and methods, you can add functionality by implementing new methods or functions within the class. For example:</strong><br>```python<br>def double_speed(self):<br>self.speed *= 2<br>```<br><strong>5. Practical Example of Speed Doubling: If you create a `Warrior` instance with initial speed 10 and define a method `double_speed`, calling it will modify the speed attribute.</strong><br>```python<br>warrior = Character(health=100, damage=50)<br>print(warrior.double_speed())  # Output: speed becomes 20<br>```<br>This summary highlights the importance of object-oriented programming concepts in Python, emphasizing how classes can be used to create reusable and modular code.<br>"
        #return jsonify({"message": "URL received successfully","a_yt_url":youtube_url, "transcript": text_data, "summary": summary}), 200
        
        return jsonify({"summary": data}), 200
    

    @app.route("/api/upload_file", methods=["POST"])
    def upload_file():
        try:
            data = request.get_json()

            youtube_url = data["url"]

            video_URL = str(youtube_url)
            destination = "./audio_files"
            final_filename = "speech1"
            download.download_mp3(video_URL, destination, final_filename)

            # Directly download and upload to MongoDB
            LOCAL_AUDIO_DIR = "./audio_files"
            destination = LOCAL_AUDIO_DIR
            final_filename = "speech1"

            local_file_path = os.path.join(destination, f"{final_filename}.mp3")

            upload.upload_to_mongodb(local_file_path, final_filename)

            return jsonify({"message": "Uploaded Successfully" ,"a_yt_url":youtube_url}), 200
        
        except Exception as e:
            
           return jsonify({"error": str(e)}), 500
        
    @app.route("/api/get_file", methods = ["GET"])
    def get_file():
        try:
            data = getFile.get_latest_audiofile()
            return jsonify({"message": "Uploaded Successfully" ,"a_yt_url":data}), 200
        except Exception as e:

            print("Error in getting file!")
            return jsonify({"error": str(e)}), 500