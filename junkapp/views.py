from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from view_helper import obj_creator, form_validator
from junkapp.models import ItemsPost, MyUser
from junkapp.forms import create_user_form, create_item_form

def index(request):
    posts = ItemsPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def item_detail_view(request, id):
    post = ItemsPost.objects.get(id=id)
    return render(request, 'item_detail.html', {'post': post})

def items_by_date_view(request):
    posts = ItemsPost.objects.order_by('-date_and_time')
    return render(request, 'items_by_date.html', {'posts': posts})

def not_claimed_view(request):
    posts = ItemsPost.objects.filter(claimed=False)
    return render(request, 'claimed.html', {'posts': posts})

def category_view(request, category):
    posts = ItemsPost.objects.filter(items=category)
    return render(request, 'category.html', {'posts': posts})

def login_view(request):
    form = login_form()
    return render(request, 'forms.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def create_user_view(request):
    form_validator('user')
    form = create_user_form()
    return render(request, 'forms.html', {'form': form})

@login_required
def create_item_view(request):
    form_validator('item')
    form = create_item_form()
    return render(request, 'forms.html', {'form': form})
