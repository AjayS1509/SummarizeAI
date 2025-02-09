
import whisper

def whisper_model():

    try:
        audio_file = "./audio_files/speech1.mp3"
        whisper_model = whisper.load_model("small")
        result_ADO = whisper_model.transcribe(audio_file)

        return result_ADO

    except:

        return "Error in whisper"