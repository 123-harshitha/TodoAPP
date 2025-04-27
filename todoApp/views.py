from django.shortcuts import redirect       #When a user visits the index page, they will be redirected to the "/todos" page.

def index(request):
    return redirect('/todos')