from django.urls import path

from cats.views import APICat, hello

urlpatterns = [
   path('cats/', APICat.as_view()),
   path('hello/', hello),
]


