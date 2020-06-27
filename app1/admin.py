from django.contrib import admin

# Register your models here.

from .models import Employee, Blog, Entry, Author
''' we can also write "app1.models" but both "models.py" and "admin.py" file present in same folder under base directory "Django1" so need 
   to write like this , we can write directly'''

admin.site.register(Employee)
''' - admin(directory)
           - site(sub-directory)
                  - register(function) 
                            - models(Employee i.e. model_name) '''
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
<!-- admin.py file commenting in html done like this -->
