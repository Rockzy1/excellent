from django.url import path
from . import views 

#urlConfiguration
urlpatterns = [
    path("hello_world/hello", views.say_hello)
]

