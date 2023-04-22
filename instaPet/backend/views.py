from django.shortcuts import render
from .forms import CommentForm
# Create your views here.

def calculateLovePercentage(request):
    return render(request, 'calculateLovePercentage.html')


