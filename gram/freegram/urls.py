from django.urls import path
from . import views

app_name ='freegram'

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("post",views.createPost.as_view(),name="create"),
    path("<str:slug>",views.DetailView.as_view(),name="details"),
    path("<str:slug>/update",views.update.as_view(),name="update"),
    path("user/create",views.createuser.as_view(),name="createuser"),
    path("<str:slug>/update/user",views.updateuser.as_view(),name="updateuser"),

]