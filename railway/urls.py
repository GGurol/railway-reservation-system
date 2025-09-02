# railway/urls.py

from django.contrib import admin
from django.urls import path, include
from reservation import views as reservation_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Set the homepage to the train list
    path('', reservation_views.index, name='home'),
    # Include all other app-specific URLs under the /reservation/ prefix
    path('reservation/', include('reservation.urls')),
]