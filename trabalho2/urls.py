"""MeuSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

urlpatterns = [

    path('admin/', admin.site.urls),
    path('todo/', include('todoList.urls')),
    path('accounts/', views.homeSec, name="sec-home"),
    path('accounts/registro', views.registro, name="sec-registro"),
    path('accounts/login/', LoginView.as_view(template_name="registro/login.html"), name="sec-login"),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name="sec-logout"),
    path('accounts/profile/', views.paginaSecreta, name="sec-paginaSecreta"),
    path('accounts/passwordChange/', PasswordChangeView.as_view(template_name="registro/passwordChangeForm.html",
    success_url=reverse_lazy('sec-passwordChangeDone')), name="sec-passwordChange"),

    path('accounts/passwordChangeDone/', PasswordChangeDoneView.as_view(template_name="registro/passwordChangeDone.html"),
     name="sec-passwordChangeDone"),

    path('accounts/updateProfile/<int:pk>', UpdateView.as_view(
    template_name="registro/updateProfile.html",
    success_url=reverse_lazy("sec-paginaSecreta"), model=User, fields=['first_name', 'last_name', 'email']),
     name="sec-updateProfile"),


     path('account/passwordReset', PasswordResetView.as_view(
         template_name="registro/passwordReset.html",
         success_url=reverse_lazy("sec-passwordResetDone"),
         from_email="webmaster_do_site@example.com.br",
         subject_template_name="registro/passwordResetSubject.txt",
         email_template_name="registro/passwordResetEmail.html"
     ),
     name="sec-passwordReset"),

     path('account/passwordResetDone', PasswordResetDoneView.as_view(template_name="registro/passwordResetDone.html"),
     name = "sec-passwordResetDone"),

     path('account/passwordResetConfirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name="registro/passwordResetConfirm.html",
            success_url=reverse_lazy("sec-passwordResetComplete")
        ),
         name="sec-passwordResetConfirm"),

     path('accounts/passwordResetComplete/', PasswordResetCompleteView.as_view(
        template_name='registro/passwordResetComplete.html'
     ), name='sec-passwordResetComplete'),

     path('accounts/verificaUsername', views.verificaUsername, name="sec-verificaUsername"),



    # path('', views.home, name='home'),
]
