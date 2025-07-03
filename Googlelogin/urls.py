from django.urls import path
from .views import GoogleLoginView,CustomUserView,Getview,LoginView,UpdateView,DeltePostByUserView
from .views import PostedJobListCreateView, PostedJobDetailView,JobTitleSuggestionView,SavedPostsByUserView,Savedpost
urlpatterns = [
    path('Savedpost/<str:user_id>/',SavedPostsByUserView.as_view(), name='Saved-post-By-user'),
    path('Saveddelete/<str:job_id>/',DeltePostByUserView.as_view(), name='Saved-post-By-user'),
    path('Saved-post/',Savedpost.as_view(), name='Saved-post'),
    path('poste-job/',PostedJobListCreateView.as_view(), name='posted-jobs-list-create'),
    path('posted-jobs/<int:pk>/',PostedJobDetailView.as_view(), name='posted-job-detail'),
    path('google-login/',GoogleLoginView.as_view(), name='google-login'),
    path('Registerpost/',CustomUserView.as_view(), name='Registration-post'),
    path('Registerpost/<int:pk>/',Getview.as_view(), name='get-object'),
    path('login/', LoginView.as_view(), name='get-object'),
    path('update/<int:pk>/',UpdateView.as_view(), name='get-object'),
    path('jobs/suggestions/',JobTitleSuggestionView.as_view(), name='job-title-suggestions'),
]