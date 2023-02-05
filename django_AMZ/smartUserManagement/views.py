from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

#imports from custom apps
from django.utils.decorators import method_decorator
from smartUserManagement.decorator import unauthenticated_user, allowed_users

# def login_view(request):
#     template = 'admin/login.html'
#     form = LoginForm
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 messages.success(request, "You have logged in!")
#                 return redirect('home')
#             else:
#                 messages.warning(request, "Your account is disabled!")
#                 return redirect('/login')
#         else:
#             messages.warning(request, "The username or password are not valid!")
#             return redirect('/login')
#     context = {'form': form}
#     return render(request, template, context)

# @login_required(redirect_field_name='next', login_url='/login')
# def bar(request):
#     template = 'pos/bar.html'
#     drink = OrderItem.objects.filter(product__catgory__gt=1).order_by('-created')
#     context = {'drink': drink}
#     return render(request, template, context)