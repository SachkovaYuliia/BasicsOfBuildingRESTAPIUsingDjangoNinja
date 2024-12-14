from django.urls import path
from . import views


urlpatterns = [
    path("", views.ninja_api.urls),

]
