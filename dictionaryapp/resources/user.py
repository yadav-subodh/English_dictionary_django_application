from .. models import User

"""
this function adds new contact to User table in database
"""


def add_new_contact(name, email, comments):
    try:
        user_object = User(name=name, email=email, comments=comments)
        user_object.save()
        return {'message': "Thank you, we will contact you soon"}
    except Exception as exception:
        print("<---- There is some exception Please Check ---->", exception)
        return {'message': "something went wrong, please try again after sometime"}
