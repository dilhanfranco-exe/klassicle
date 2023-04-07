from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    all_members = Member.objects.all
    return render(request, 'index.html', {'all': all_members})