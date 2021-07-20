

# Elasticsearch and Redis in Django. 
Project to test Elasticsearch and Redis with Django.

# Requirements
    asgiref==3.3.4
    certifi==2021.5.30
    Django==3.2.4
    django-elasticsearch-dsl==7.2.0
    django-elasticsearch-dsl-drf==0.22.1
    django-environ==0.4.5
    django-nine==0.2.4
    djangorestframework==3.12.4
    elasticsearch==7.13.1
    elasticsearch-dsl==7.3.0
    gunicorn==20.1.0
    # pkg-resources==0.0.0
    psycopg2==2.9.1
    python-dateutil==2.8.1
    python-decouple==3.4
    pytz==2021.1
    six==1.16.0
    sqlparse==0.4.1
    urllib3==1.26.5
    whitenoise==5.2.0

# Installation
Steps to build, load data from fixtures and run project:
   # Django Virtual Environment Setup
    1. Install Package
        apt-get install python3-venv      
    2. Create a Directory
        mkdir djangoenv
    3. Create Virtual Environment
        python3 -m venv djangoenv  
    4. Activate Virtual Environment
        source djangoenv/bin/activate 

   # Install Django
    python -m pip install Django
   # Install Djangorestframework
    djangorestframework==3.12.4
   # Install Elasticsearch dsl
    django-elasticsearch-dsl==7.2.0
    django-elasticsearch-dsl-drf==0.22.1
   # Installing Redis
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make 

# Features
    Redis is an open source, in-memory data structure store, used as a database, cache, and message broker. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams.

    Elastic Search
    The speed and scalability of Elasticsearch and its ability to index many types of content mean that it can be used for a number of use cases:

       1. Application search
       2. Website search
       3. Enterprise search
       4. Logging and log analytics
       5. Infrastructure metrics and container monitoring
       6. Application performance monitoring
       7. Geospatial data analysis and visualization
       8. Security analytics
       9. Business analytics
# Usage example
    from django.shortcuts import render
    from django.http import HttpResponse
    from .models import *
    from django.conf import settings
    from django.core.cache.backends.base import DEFAULT_TIMEOUT
    from django.views.decorators.cache import cache_page
    from django.core.cache import cache

    CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

    def get_recipe(filter_recipe = None):
        if filter_recipe:
            print("DATA COMING FROM DB")  
            recipes = Recipe.objects.filter(name__icontains = filter_recipe)
        else:
            recipes = Recipe.objects.all()
        return recipes

    def home(request):
        filter_recipe = request.GET.get("recipe")
        print("filter_recipe", filter_recipe)
        if cache.get(filter_recipe):
            print("Data coming from Cache")
            recipe = cache.get(filter_recipe)
        else:
            if filter_recipe:
                recipe = get_recipe(filter_recipe)
                cache.set(filter_recipe, recipe)
            else:
                recipe = get_recipe()

        context = {'recipe': recipe}  
        return render(request, "redis_app2/home.html", context)

# Running the Project
    # start the elasticsearch engine
    sudo systemctl start elasticsearch.service
    
    python manage.py runserver 127.0.0.1:8000

# Deployment Notes
    When you deploy to Heroku, the dependencies you specify in your requirements.txt file are automatically installed before app startup.

    If you’re using Django, the collectstatic command also runs automatically during the deployment process. This command can be tricky to configure properly. To make it easier, add the Django-Heroku Python package, which sets up everything for you.

    To automatically perform other tasks (such as any required database migrations) before your app is deployed, you can add a release phase command to your app.

# Tech Stack / Built With
    Framework = Django
    Technology = Python

# Authors
    Anurag Nadda is the Python Developer. Anurag was born and raised in the Bilaspur(H.P.). He was a Mechanical Engineer before shifting to development.
    You can chat with Anurag Nadda on Twitter or Instagram at @anuragnadda or check out his website at <a www.anuragnadda.com> 
# License
    This concludes your stunning README. Don’t forget to star the repository. Create awesome documentation and help this community grow with full speed. If you want to add or edit any section send PRs :)

# Flow Diagram
<img src="/Flow Diagram.png" alt="My cool logo"/>
