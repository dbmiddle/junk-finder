from junkapp.forms import LoginForm, SignUpForm, CreateItemForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .view_helper import obj_creator, object_form_validator
from junkapp.models import ItemsPost, MyUser

# Regarding additional text that might be needed for individual
# form views, it would be necessary to define them in the view
# and add them to the render dictionary.
def login_view(request):
    form = LoginForm()
    return render(request, 'login.html', {"form": form})


def signup(request):
    form = SignUpForm()
    return render(request, 'forms.html', {'form': form})


# class ItemPostView(CreateView):
#     def get(self, request):
#         context = {
#             'data': ItemsPost.objects.all()
#         }
#         return render(request, 'templates/home.html', context)

#@login_required(login_url='/login/')
def home(request):
    posts = ItemsPost.objects.all()
    return render(request, 'home.html', {'data': posts})


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", reverse('login')))


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

@login_required
def create_item_view(request):
    form = CreateItemForm()
    return render(request, 'forms.html', {'form': form})
