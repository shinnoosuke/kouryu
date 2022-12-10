from django.shortcuts import render
from .models import Review

def review_list(request):
    context = {
        'review_list': Review.objects.all(),
    }
    return render(request,'reviews/review_list.html', context)