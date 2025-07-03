from django.urls import path
from .views import CustomResumeCreateOrUpdateView,CustomResumeDetailView

urlpatterns = [
    path("custom-resume/", CustomResumeCreateOrUpdateView.as_view()),
    path("resume-detail/", CustomResumeDetailView.as_view()),
    
]
