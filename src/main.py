from helper.apiConfig import request
from config.apiNames import API_NAMES
from helper.storeCSV import storeInCSV
from src.analyze import analyzeData

def dataAnalyzer():
    try:
        data = request(API_NAMES["dummyUserApi"]) 
        storeInCSV(data["users"])
        print(analyzeData(data["users"]))
    except Exception as e:
        print("Unable to Analyze data", e)

if __name__ == "__main__":
    dataAnalyzer()