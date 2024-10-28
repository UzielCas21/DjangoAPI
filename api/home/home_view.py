from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGING_URL

# Create your views here.
@login_required(login_url='/login')
def home_view(request):
    template_name = "html/index.html"
    
    return render(request,template_name)