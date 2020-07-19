from django.conf.urls import url
from web.index import views

urlpatterns = [
    url(r"^$", views.Dashboard.as_view(), name="dashboard"),
    url("user", views.User.as_view(), name="user"),
]
