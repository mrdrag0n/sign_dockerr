from django.urls import path
from .views import ProfileList, ProfileDetail, ProfileCreate, ProfileUpdate, ProfileDelete, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', ProfileList.as_view(), name='profiles'),
    path('Profile/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profil-create/', ProfileCreate.as_view(), name='cert-create'),
    path('profil-update/<int:pk>', ProfileUpdate.as_view(), name='profile-update'),
    path('delete-cert/<int:pk>', ProfileDelete.as_view(), name='delete-cert')
]