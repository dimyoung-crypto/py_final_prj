import django.urls
from . import views

urlpatterns = [
    django.urls.path("", views.project_index, name="project_index"),
    django.urls.path("<int:pk>/", views.project_detail, name="project_detail"),
]
