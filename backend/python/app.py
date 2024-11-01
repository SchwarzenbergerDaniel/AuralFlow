import youtube_api
from flask import Flask, request, jsonify

app = Flask(__name__)

# TOOD: TRY CATCH AND DELTE FILE

@app.route('/upload_from_url', methods=['POST'])
def upload_youtube():
    data = request.json
    if 'url' not in data:
        return jsonify({"error": "No URL provided"}), 400
    url = data["url"]
    if(youtube_api.uploadFromURL(url)):
        return 200
    else:
        return 400

if __name__ == "__main__":
    app.run()