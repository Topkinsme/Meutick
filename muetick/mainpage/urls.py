from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("adminpage/",views.adminpage,name="adminpage"),
    path("catpage/",views.catpage,name="catpage"),
    path("dev/",views.dev,name="dev"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("profile/",views.profile,name="profile"),
    path("signin/",views.signin,name="signin"),
    path("signup/",views.signup,name="signup"),
    path("landingpage/",views.landingpage,name="landingpage"),
]