import pymongo
import time
import ast
from dotenv import load_dotenv,find_dotenv
from bson.objectid import ObjectId
import os
from flight_search import FlightSearch
load_dotenv(find_dotenv())
password=os.environ.get("MONGO_DB_PASSWORD")
class alert_data:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(f"mongodb://trex49001:{password}@ac-gjyhwip-shard-00-00.sk7cnrz.mongodb.net:27017,ac-gjyhwip-shard-00-01.sk7cnrz.mongodb.net:27017,ac-gjyhwip-shard-00-02.sk7cnrz.mongodb.net:27017/?ssl=true&replicaSet=atlas-ni4uh5-shard-0&authSource=admin&retryWrites=true&w=majority")
        self.db = self.client.flightdata
        self.db_collection=self.db.data

        
    def add_alert(self,list):
        list[0]=ast.literal_eval(list[0])
        alert={'flightno': list[0]["flightno"], 'from': list[0]["from"], 'to': list[0]["to"], 'fare': list[0]["fare"], 'dept': list[0]["dept"], 'arrival': list[0]["arrival"], 'phone':list[1][0],'email':list[1][-1]}
        print(alert)
        self.db_collection.insert_one(alert)
        print("db_upd")


    def delete_alert(self,id):
        bsid=ObjectId(id)
        self.db_collection.delete_one({"_id":bsid})



    def change_alert(self):
        rate_finder=FlightSearch("yR4u41N6V4InhVEL3Z0EwMfu4ti4lLx-")
        data=self.db_collection.find({})
        for i in data:
            data_price=i["fare"]
            date=i["dept"][0]
            date_formatted=f"{date[-2]}{date[-1]}/{date[5]}{date[6]}/{date[0]}{date[1]}{date[2]}{date[3]}"
            ltp=last_traded_price=rate_finder.flight_specific_rate(from_place=i["from"],to_place=i["to"],date=date_formatted,flight_no=i["flightno"],dept=i["dept"],arrival=i["arrival"])
            if ltp==None:
                pass
            if ltp>data_price:
                print("price_incr")
                self.delete_alert(i["_id"])
                
            if ltp<data_price:
                print("price_dec")
                self.delete_alert(i["_id"])




db=alert_data()
db.change_alert()
