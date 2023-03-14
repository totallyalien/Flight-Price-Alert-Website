import pymongo
import time
import ast
from dotenv import load_dotenv,find_dotenv
from bson.objectid import ObjectId
import os
from flight_search import FlightSearch
from notification_manager import MailAlert




load_dotenv(find_dotenv())
password=os.environ.get("MONGO_DB_PASSWORD")
username=os.environ.get("MONGO_DB_USERNAME")
kiwi_api=os.environ.get("KIWI_API_KEY")
mail_id=os.environ.get("MY_MAIL")
mail_pass=os.environ.get("MAIL_PASSWORD")


class alert_data:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(f"mongodb://{username}:{password}@ac-gjyhwip-shard-00-00.sk7cnrz.mongodb.net:27017,ac-gjyhwip-shard-00-01.sk7cnrz.mongodb.net:27017,ac-gjyhwip-shard-00-02.sk7cnrz.mongodb.net:27017/?ssl=true&replicaSet=atlas-ni4uh5-shard-0&authSource=admin&retryWrites=true&w=majority")
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
        print("data_check_running")
        rate_finder=FlightSearch(kiwi_api)
        data=self.db_collection.find({})
        for i in data:
            data_price=i["fare"]
            date=i["dept"][0]
            date_formatted=f"{date[-2]}{date[-1]}/{date[5]}{date[6]}/{date[0]}{date[1]}{date[2]}{date[3]}"
            ltp=rate_finder.flight_specific_rate(from_place=i["from"],to_place=i["to"],date=date_formatted,flight_no=i["flightno"],dept=i["dept"],arrival=i["arrival"])
            print(ltp)
            if ltp==None:
                pass
            elif ltp[0]>data_price:
                mail=MailAlert(mail=mail_id,password=mail_pass)
                mail.send_mail(i["from"],i["to"],data_price,ltp[0],i["email"],ltp[1],i["flightno"])
                print("price_incr")
                self.delete_alert(i["_id"])
                
            elif ltp[0]<data_price:
                mail=MailAlert(mail=mail_id,password=mail_pass)
                mail.send_mail(i["from"],i["to"],data_price,ltp[0],i["email"],ltp[1],i["flightno"])
                print("price_dec")
                self.delete_alert(i["_id"])


