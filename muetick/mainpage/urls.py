from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.dashboard, name="dashboard"),
    path("adminpage/",views.adminpage,name="adminpage"),
    path("catpage/<str:mname>",views.catpage,name="catpage"),
    path("dev/",views.dev,name="dev"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("profile/",views.profile,name="profile"),
    path("signin/",views.signin,name="signin"),
    path("signup/",views.signup,name="signup"),
    path("",views.landingpage,name="landingpage"),
]