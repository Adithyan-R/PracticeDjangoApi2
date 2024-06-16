from api1 import views
from django.urls import path

urlpatterns =[
    path('tutorial/', views.TutorialList.as_view()),
    path('tutorial/<int:pk>/', views.TutorialDetails.as_view()),
]

