from django.contrib import admin    # Register the todos model in the admin panel 
from .models import Todo

admin.site.register(Todo)

