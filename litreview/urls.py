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
    path('ticket/posts/', tickets.views.posts, name='posts'),
    path('ticket/create/', tickets.views.ticket_create, name='ticket_create'),
    path('ticket/review/create/', tickets.views.ticket_and_review_upload, name='ticket_and_review_upload'),
    path('ticket/<int:ticket_id>/', tickets.views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/update/', tickets.views.ticket_update, name='ticket_update'),
    path('ticket/<int:ticket_id>/delete/', tickets.views.ticket_delete, name='ticket_delete'),
    path('tickets/<int:ticket_id>/review/create/', tickets.views.review_create, name='review_create'),
    path('tickets/review/list/', tickets.views.review_list, name='review_list'),
    path('tickets/<int:ticket_id>/review/<int:review_id>/', tickets.views.review_detail, name='review_detail'),
    path('tickets/<int:ticket_id>/review/<int:review_id>/update/', tickets.views.review_update,
         name='review_update'),
    path('tickets/<int:ticket_id>/review/<int:review_id>/delete/', tickets.views.review_delete,
         name='review_delete'),
    path('follow-user/', authentication.views.follow_user, name='follow_user'),
    path('unfollow-user/<int:user_id>', authentication.views.unfollow_user, name='unfollow_user'),
    path('block_user/<int:user_id>/', authentication.views.block_user, name='block_user'),
    path('unblock_user/<int:user_id>/', authentication.views.unblock_user, name='unblock_user'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
