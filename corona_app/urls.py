from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('donnees_par_pays', views.donnees_par_pays, name='donnees_par_pays'),
    path('apropos', views.apropos, name='apropos'),
    path('nbr_cas_conf', views.cas_conf, name='nbr_cas_conf'),
    path('nbr_deces', views.cas_deces, name='nbr_deces'),
    path('nbr_tests', views.tests, name='nbr_tests'),
    path('act_medias', views.act_medias, name='act_medias'),
    path('act', views.act, name='act'),
    path('medias_sociaux', views.medias_sociaux, name='medias_sociaux'),
    path('info', views.info, name='info'),
    path('analyses', views.analyses, name='analyses'),
]
