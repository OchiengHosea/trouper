from django.urls import path, re_path
import accounts.views as acc_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('login/', acc_views.LoginView.as_view(), name='login'),
    re_path(r'^login/$', acc_views.LoginView.as_view(), name='login'),

]