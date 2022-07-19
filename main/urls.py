from django.urls import path
from .views import HomePageView, ProfileView, image_base_delete_item, image_upload_view, predict
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('upload', image_upload_view, name = 'upload'),
    path('predict/<int:pk>', predict, name= 'predict'),
    path('profile', ProfileView.as_view(), name = 'profile'),
    path('profile/<int:pk>/delete/', image_base_delete_item, name='imagebase_delete'),
    # path('history', HistoryView.as_view(), name = 'history'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)