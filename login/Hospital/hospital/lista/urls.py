from django.conf.urls import url,re_path
from django.urls import path, include
from lista import views

urlpatterns =[

url(r'lista/pacientes/',views.usuarios_listpa,name="listpaciente"),
url(r'lista/personal/',views.usuarios_listen, name="listenfermero"),
url(r'lista/tutor/',views.usuarios_listu, name="listtutor"),
url(r'logout/',views.logout_view,name="logout")
]