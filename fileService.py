from datetime import datetime
import os
from io import BytesIO


def getFileName(base_name="MusicalInstrumentsScraper", file_format = ".xlsx"):
    current_time = datetime.now().strftime("%Y-%m-%d %H-%M")
    filename =  base_name + current_time + file_format
    print("file name " + filename)
    return filename

def getFullFileName(filename=""):
    if(filename==""):
        filename = getFileName()
    # get the absolute path of the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # construct the path to save the Excel file
    file_path = os.path.join(script_dir, filename)
    return file_path

def getFileStream(workbook):
    if workbook is None:
        return None
    filestream = BytesIO()
    workbook.save(filestream)
    filestream.seek(0)
    return filestream
