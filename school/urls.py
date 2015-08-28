from django.conf.urls import include, url
from school import views
urlpatterns = [
        url(r'^marks/$', views.MarksView.as_view()),
        url(r'^reg_user/$',views.reg_user),
]