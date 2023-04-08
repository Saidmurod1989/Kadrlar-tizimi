

from django.urls import path

# url - bu project bilan app larni manzillarini bir biriga bog'laydi.
# Models fayl - kerakli modellarni yozadi, admin.py - uni admin panelda korsatadi. views fayl frontend qismi uchun foydalanuvchiga ko'rsatadi. url - manzillarini biri biriga ulaydi

from django.conf import settings
from django.conf.urls.static import static
from .views import HodimlarView

urlpatterns = [
    path('', HodimlarView.as_view(), name='hodim')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# STATIC - bu frontendda ranglar, turli media va grafik bilan ishlaydigan qismi
# MEDIA - bu frontendda rasmlar videolar bilan ishlaydigan qismidir



