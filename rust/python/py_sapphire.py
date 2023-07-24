from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from isodate import parse_duration
app = Flask(__name__)



from string_conversion import join_most_sophisticated_sentences,modify_transcript,get_string_format,get_youtube_video_duration,sent_tokenize


@app.route("/get_transcript/<videoID>",methods=["GET"])
def get_transcript(videoID):
    json_list = YouTubeTranscriptApi.get_transcript(videoID, languages=["en", "en-US"])
    string_format = get_string_format(json_list)
    transcript = modify_transcript(60, 6000, videoID, string_format)
    print(len(sent_tokenize(transcript)))
    return {"transcript":transcript.lower(),"sent_tokens":sent_tokenize(transcript)}



if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=8000)
