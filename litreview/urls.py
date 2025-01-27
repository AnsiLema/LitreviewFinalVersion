"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import reviews.views
import tickets.views
import tickets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='authentication/login.html',
                               redirect_authenticated_user=True
                               ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', reviews.views.home, name='home'),
    path('ticket/list/', tickets.views.ticket_list, name='ticket_list'),
    path('ticket/create/', tickets.views.ticket_create, name='ticket_create'),
    path('ticket/review/create/', tickets.views.ticket_and_review_upload, name='ticket_and_review_upload'),
    path('ticket/<int:ticket_id>/', tickets.views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/update/', tickets.views.ticket_update, name='ticket_update'),
    path('ticket/<int:ticket_id>/delete/', tickets.views.ticket_delete, name='ticket_delete'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)