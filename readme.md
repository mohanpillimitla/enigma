A simple nested serializer

Django:Django is an orm which is an object relational model which means by creating classes we can create tables in the database .we dont need to write raw sql queries in django

serializer is used for creating serialized json data in django.It serializes the model by taking the queryset in the view.

In order to define nested serializers we have to define a related_name field in the model in which it is related as foreignkey 

hence it can used as a field in the other serializer  and adding many=True in the main serializer will do the job for us


Using this serializer we can create api end points which can fetched from ajax or can be used for single page applications like  

react or angular





loading the initial data :

we will load the initial data into the table using the command

we will use the concept of fixtures in django for loading data into the database



python manage.py loaddata user.json

This command will load the user data into the database 

we can also dump data to json using


python manage.py dumpdata appname.model --format json --indent 2 > filename(ubuntu)




