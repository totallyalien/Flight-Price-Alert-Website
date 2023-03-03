import requests
endpoint="https://api.tequila.kiwi.com/v2/search?"

class FlightSearch:

    def __init__(self,api) -> None:
        self.apikey=api
        
    

    def rate(self):
        header={
            "apikey":self.apikey,
        }

        body={ 
            "fly_from":"LGA",
            "fly_to":"MIA",
            "dateFrom":"10/03/2023",
            "dateTo":"12/03/2023",
        }

        response=requests.get(url=endpoint,params=body,headers=header)
        print(response.json())


x=FlightSearch("yR4u41N6V4InhVEL3Z0EwMfu4ti4lLx-")

x.rate()