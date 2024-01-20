# students/urls.py
from django.urls import path
from .views import index, student_detail, generate_qr_code

urlpatterns = [
    path('', index, name='index'),
    # path('test/<str:student_id>', generate_qr_code),
    path('student/<str:student_id>/', student_detail, name='student_detail'),
]
