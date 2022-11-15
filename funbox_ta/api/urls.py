from django.urls import path
from .views import visited_domains, visited_links

urlpatterns = [
    path('visited_links', visited_links, name='visited_links'),
    path('visited_domains', visited_domains, name='visited_domains')
]
