from flask import Flask, jsonify, request, make_response, send_file
from flask_cors import CORS
import MusicalInstrumentsScraper
from fileService import getFileName, getFullFileName
import uuid
from webdriver_manager.chrome import ChromeDriverManager

#import sys

#sys.path.append(".")

app = Flask(__name__)

CORS(app)

files_dict = {}


@app.route("/")
def index():
    return getServerResponse(message="Musical Instruments Scraper is Ready")


@app.route("/websites")
def websites():
    print("received a request to get the supported websites")
    webs = MusicalInstrumentsScraper.getAllowedWebsites()
    return getServerResponse(data=webs)

@app.route("/scrap", methods=['POST'])
def scrap():
    print("called scrap")
    webs_to_scrap = postRequestWebsList()
    #generate the excel
    if not webs_to_scrap:
        return getServerResponse(error="Server did not receive the list of URLs to scrap")
    try:
        stream = MusicalInstrumentsScraper.scrapToExcelConcurrently(webs_to_scrap)
        file_id = getFileID(stream)
        return getServerResponse(file_ready=True, file_id=file_id)
    except Exception as e:
        print("exception in trying to scrap")
        return getServerResponse(file_ready=False, error=str(e))



@app.route("/download/<file_id>")
def download(file_id):
    print("received a download request")
    file_stream = files_dict.get(file_id)
    if file_stream is None:
        return "File not found", 404
    return send_file(file_stream, as_attachment=True, download_name= getFileName())


def getFileID(filestream):
    file_id = str(uuid.uuid4())
    files_dict[file_id] = filestream
    return file_id

def postRequestWebsList():
    try:
        webs_to_scrap = request.get_json().get('webs_to_scrap')
        return webs_to_scrap
    except Exception as e:
        print(e)
        return None
    
def getServerResponse(ready=True, message=None, data=None, error=None, file_ready=False, file_id=None):
    return jsonify({
        "ready": ready,
        "message": message,
        "data": data,
        "error": error,
        "file_ready": file_ready,
        "file_id": file_id
    })



if __name__ == '__main__':
    app.run(debug=True)
