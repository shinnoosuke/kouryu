from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewCreateForm

def review_list(request):
    context = {
        'review_list': Review.objects.all().order_by('-created_at'),
    }
    return render(request,'reviews/review_list.html', context)

def review_create(request):
    #return render(request, 'reviews/review_form.html')
    context = {
        'form': ReviewCreateForm()
    }
    return render(request, 'reviews/review_form.html', context)

def review_create_send(request):
    #name = request.POST.get('store_name') 
    #print('送信されたデータ→{}' .format(name))
    form = ReviewCreateForm(request.POST)
    form.save()
    return redirect('reviews:review_list')

    context = {
        'form': ReviewCreateForm()
    }
    return render(request, 'reviews/review_form.html', context)

def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {
        'review' : review,
    }
    return render(request,'reviews/review_detail.html', context)

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('reviewss:review_list')

    context = {
        'review': review
    }         
    #return render(request, 'review_confirm_delete.html', context)
    return render(request, 'reviews/review_confirm_delete.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewCreateForm(request.POST or None, instance=review)
    if request.method == 'POST' and form.is_valid():
        review.delete()
        return redirect('reviews:review_list')

    context = {
        'form': form
    }         

    return render(request, 'reviews/review_form.html', context)

#def review_create(request):
#    form = ReviewCreateForm(request.POST or None)
#    if request.method == 'POST' and form.is_valid():
#        form.save()
#        return redirect('review:review_list')

#    context = {
#        'form':form
#    }       
#    return render(request, 'reviews/review_form.html', context)