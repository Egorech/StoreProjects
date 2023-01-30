from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import User, EmailVerification
from product.models import Basket
from  users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
# Create your views here.
from django.contrib import auth, messages
from common.views import TitleMixin


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login.html')
    success_message = 'Вы успешно зарегестрированы!!!'
    title = 'Store-Регистрация'


"""
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome!!!!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
"""

class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store-Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

"""
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance = request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)

    context = {'title': 'Профиль',
               'form': form,
               'baskets': Basket.objects.all(),
               'total_sum': total_sum,
               'total_quantity': total_quantity,
               }
    return render(request, 'users/profile.html', context)
"""

class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))