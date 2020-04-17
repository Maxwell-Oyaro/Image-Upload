from django.urls import path
from .views import IndexPageView, UploadPageView

#configuring views urls
app_name = 'image'
urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('upload/', UploadPageView.as_view(), name='upload')
]