from django.conf.urls import patterns, url
from User_Profile import views

urlpatterns = patterns('',
                        
url(r'^', views.register, name='register'),
url(r'^dashboard', 'User_Profile.views.user_dashboard', name='user_dashboard'),
url(r'^matches', 'Matches.views.matches', name='matches'),   
url(r'^buddy', 'User_Profile.views.buddy', name='buddy'),
)

