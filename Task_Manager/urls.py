from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from staff.views import *
from projects.views import *

urlpatterns = [
    path("super_admin/", admin.site.urls),
    path('sign_up', sign_up),
    path('login', login_process),
    path('change_password', change_user_paasword),
    path('main/projects', main),
    path('main/add_project', add_project)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
