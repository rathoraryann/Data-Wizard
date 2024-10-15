from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('get-resume/<int:id>', views.get_resume), 
    path('create-resume/', views.create_resume), 
    path('update-resume/<int:id>', views.update_resume),
    path('delete-resume/<int:id>', views.delete_resume),
    path('predict/<int:id>', views.predict_skills),
]
