from django.conf.urls import url,re_path
from django.urls import path, include
from usuarios import views

urlpatterns =[

path('registrar/',views.Registro_View, name="registro" ),
url(r'perfil/',views.PerfilView,name="perfil"),
url(r'editar/(?P<usuario_id>\d+)$',views.perfil_edit, name="perfil_editar"),
url(r'tutor/datos/(?P<perfil>\d+)$',views.Tutor_view, name="tutor_form"),
url(r'paciente/datos/(?P<perfil>\d+)$',views.Paciente_view, name="paciente_form"),
url(r'personal/datos/(?P<perfil>\d+)$',views.Personal_view, name="personal_form"),
]