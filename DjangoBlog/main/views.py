from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.views.generic import ListView, CreateView

class Homepage(ListView):
    template_name= "main/categories.html"
    model = TutorialCategory
    context_object_name ='categories'

def about(request):
    return HttpResponse("About me: I am Laiba Tanveer Ahmed Aryal Jutt")

class FilterSeries(ListView):
    template_name = "main/category.html"
    model = TutorialSeries
    context_object_name= 'category'

    
    def get_queryset(self, *args, **kwargs):
       return TutorialSeries.objects.filter(tutorial_category__category_slug=self.kwargs['first_slug'])
            
class FilterTutorials(ListView):
    template_name = "main/tutorial.html"
    model = Tutorial
    context_object_name= 'tutorial'
    
             

    def get_queryset(self, *args, **kwargs):
        return Tutorial.objects.filter(tutorial_series__tutorial_series=self.kwargs['second_slug'])

class FilterBlogs(ListView):
    template_name = "main/blog.html"
    model = Tutorial
    context_object_name= 'tutorial'
    def get_queryset(self, *args, **kwargs):
        
        Tutorial.objects.filter(tutorial_slug=self.kwargs['third_slug'])
        
        return Tutorial.objects.filter(tutorial_slug=self.kwargs['third_slug'])

        # series = self.request.GET.get('q', None)
        # this_tutorial = Tutorial.objects.get(tutorial_slug=self.kwargs['second_slug'])
        # return Tutorial.objects.filter(tutorial_series__tutorial_series=series)





class Register(CreateView):
    model = Tutorial
    form_class = NewUserForm
    template_name = "main/register.html"
    success_url = '/'

class LogoutRequest(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged Out Successfully")
        return HttpResponseRedirect("/")


class LoginRequest(View):
    model = Tutorial
    form_class = AuthenticationForm
    template_name = "main/login.html"
    success_url = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
        
    def post(self,request):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                msg = messages.error(request, "Invalid username or password.")
                return HttpResponse(request, msg)
        else:
            msg =messages.error(request, "Login Failed!.")
            return HttpResponse(request, msg)
            