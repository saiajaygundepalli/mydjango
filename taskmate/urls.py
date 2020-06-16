from django.contrib import admin
from django.urls import path,include
from todolist_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('todolist/', include('todolist_app.urls')),
    path('account/',include('users_app.urls')),
    path('contact-us',views.contact,name='contact-us'),
    path('ajax',views.ajax,name='ajax'),
    path('about-us',views.about,name='about-us'),
]
