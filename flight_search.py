import requests
from data_manager import DataManager
airport_code=DataManager()




endpoint="https://api.tequila.kiwi.com/v2/search?"

#aiportlist
airport_code=DataManager()


class FlightSearch:

    def __init__(self,api) -> None:
        self.apikey=api
        
    

    def rate(self,from_place,to_place,fromdate):

        header={
            "apikey":self.apikey,
        }

        body={ 
            "fly_from":from_place,
            "fly_to":to_place,
            "dateFrom":fromdate,
            "dateTo":fromdate,
            "curr":"INR",
            "locale":"in"

        }

        response=requests.get(url=endpoint,params=body,headers=header)
        flight_details_data=[]
        data_dic=response.json()["data"]
        for i in range(0,len(response.json()["data"])):
            flight_details_data.append({"flightno":data_dic[i]["airlines"][0]+" "+str(data_dic[i]["route"][0]["flight_no"]), "from":data_dic[i]["cityFrom"],"to":data_dic[i]["cityTo"],"fare":data_dic[i]["price"],"dept":data_dic[i]["local_departure"].split("T"),"arrival":data_dic[i]["local_arrival"].split("T"),"link":data_dic[i]["deep_link"]})
        return flight_details_data


    def flight_specific_rate(self,from_place,to_place,date,flight_no,dept,arrival):
        from_place=airport_code.name_to_iata_flight_specific(from_place)
        to_place=airport_code.name_to_iata_flight_specific(to_place)
        current_data=self.rate(from_place=from_place,to_place=to_place,fromdate=date)
        for details in current_data:
            if details["flightno"]==flight_no:
                return details["fare"]
                break
        