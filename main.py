from flask import Flask,render_template,request,redirect,url_for
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import alert_data
from phone_number_validation import Number_validation
from email_validation import Email_validation
#aiportlist
airport_code=DataManager()
airport_code_diC=airport_code.airportdata_dic()


#flightsearch
search=FlightSearch("yR4u41N6V4InhVEL3Z0EwMfu4ti4lLx-")


#mongodb
db=alert_data()
flight_dic=[]

#number_valid
check_number=Number_validation()

#email_validation
check_email=Email_validation()


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index_page():
  search_result=[]
  if request.method=="POST":
    from_city=request.form.get("from")
    to_city=request.form.get("to")
    date=request.form.get("date")
    iata=airport_code.name_to_iatacode(from_city,to_city)
    search_result=search.rate(from_place=iata[0],to_place=iata[1],fromdate=f"{date[-2]}{date[-1]}/{date[5]}{date[6]}/{date[0]}{date[1]}{date[2]}{date[3]}")
  

  return render_template("index.html",airport_list=airport_code_diC,search_data=search_result)

@app.route("/add",methods=["POST","GET"])
def add_alert():
  if request.method=="POST":
    flight_dic.append(request.form["add_alert_details"])
    return redirect(url_for('add_number'))

@app.route("/add/added_succ",methods=["POST","GET"])
def add_number(): 
  if request.method=="POST":
    number=request.form.get("number")
    email=request.form.get("email")
    if check_email.email_validation(email) | check_number.number_validation(number):
      flight_dic.append([number,email])
      db.add_alert(flight_dic)
      flight_dic.clear()
    else:
      print("invalid")
  return render_template("alert.html")
  


if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)

  # tamizh on the server..