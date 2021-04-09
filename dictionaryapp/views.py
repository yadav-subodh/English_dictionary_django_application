from django.shortcuts import render
from .resources.user import add_new_contact
from .resources.superUser import get_super_user
from .resources.dictionary import add_new_word, get_all_words, get_words_by_matching

# Create your views here.
""" This end point redirects to the home page.
    Where the context is a variable which use to send data from backend
    to template.  
"""


def home(request):
    context = get_all_words()
    return render(request, 'index.html', {'data': context})


def contact(request):
    return render(request, 'contact.html')


def submit_contact_details(request):
    try:
        if request.method == 'POST':
            context = add_new_contact(name=request.POST['name'], email=request.POST['emailId'],
                                      comments=request.POST['comments'])
            return render(request, "submitContact.html", {'data': context})
    except Exception as exception:
        context = {"message": "something went wrong, please try again after some time"}
        print(exception)
        return render(request, "404_page.html", {'data': context})


def search(request):
    if request.method == 'POST':
        context = get_words_by_matching(request.POST['searchString'])
    return render(request, 'filter.html', {'data': context})


def admin_page(request):
    return render(request, 'admin.html')


"""
this end point use to login as admin 
make sure SuperUser table  has a superUser with any emailId and password
if SuperUser table don't has any row first add  one emailId and password manually 
follow the following step
1. set up all setting for django project including makemigrations and migrate
2. create superuser (django predefined) by  "python manage.py createsuperuser" command on terminal set name and password
3.  run django application by  "python manage.py runserver" command on terminal
4. go to web browser  and hit the url "http://127.0.0.1:8000/" (port number may be different)
5.add in url "/admin" like this "http://127.0.0.1:8000/admin" hit enter
6. login with name and password which is created in step 2.
7. we can see  three User, SuperUser, and Dictionary
8. select SuperUser table and add one SuperUser with any emailId and password after that 
use this emailId and Password to login as admin in Dictionary application.
"""


def admin_login(request):
    try:
        if request.method == 'POST':
            login_status = get_super_user(email=request.POST['email'], password=request.POST['password'])
            if login_status['super_user_object'] is not None:
                return render(request, 'word.html')
            else:
                response_data = {'message': login_status['message']}
                return render(request, '404_page.html', {'data': response_data})
    except Exception as exception:
        print(exception)
        return render(request, '404_page.html',
                      {'data': {'message': 'something went wrong please try again after some time'}})


def word(request):
    return render(request, 'word.html')


def add_word(request):
    try:
        if request.method == 'POST':
            context = add_new_word(word=request.POST['word'], meaning=request.POST['meaning'],
                                   synonyms=request.POST['synonyms'], antonyms=request.POST['antonyms'],
                                   usage=request.POST['usage'])
            return render(request, "submitWord.html", {'data': context})
    except Exception as exception:
        context = {"message": "something went wrong, please try again after sometime"}
        print(exception)
        return render(request, "404_page.html", {'data': context})
