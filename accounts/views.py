from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy




class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('blog:post_list')


def RegisterView(request):
    return render(request,"accounts/register.html")


