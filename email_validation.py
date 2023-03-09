import pyisemail 

class Email_validation:
    def __init__(self) -> None:
       pass 
        

    def email_validation(self,email):
        return pyisemail.is_email(email,check_dns=True)
    


