from django.db import models

# Create your models here.

# "models.py" file in "app1" folder

''' As we use "request" in "views.py" file , similarly, we used here "model inside models" . Here, whatever functions ,we are using all are present inside 
"django.db" i.e. Django database" so here is a directory named as "django" and inside this has a sub-directory "models" which contains all the models or Model
such as:
- django
      - models
            - models or Model ''' 


class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    #id = models.IntegerField(null=True)
    start_date = models.DateField(null = True)
    #"__str__" function mainly used to convert an object into a string.
    #email = models.EmailField()

    def __str__(self):
    	return str(self.first_name)
    #timestamp = models.DateTimeField()

    # "id" is the primary key which is by-default created in Django, & if you want to change it then , you can.

    '''Table | objects | condition(the thing which we have to fetch)
    blog.objects.all()
    blog.objects.get(name = 'shivam')
    blog.objects.filter()
    blog.objects.create(name = 'nishu')
    '''
class Blog(models.Model):
    """docstring for blog"""
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
        
        
