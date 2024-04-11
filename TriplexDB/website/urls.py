"""
URL configuration for TriplexDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = "home"),
    #path('search_rna_symbol', views.search_rna_symbol, name="search_rna_symbol"),
    path('search_rna_symbol', views.search_rna_symbol_values, name="search_rna_symbol"),
    path('search_promoter', views.search_promoter, name="search_promoter"),
    path('search_transcript', views.search_transcript, name="search_transcript"),
    #path('search_transcript', views.search_transcript_values, name="search_transcript"),
    path('search_rna_home', views.search_rna_home, name="search_rna_home"),
    path('search_rna_results', views.search_rna_results, name="search_rna_results"),
    path('search_gen_region_home', views.search_gen_region_home, name="search_gen_region_home"),
]