from django.shortcuts import render, redirect
from .models import User, Passwords
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AddPassword, UserUpdateForm
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(requests):
    return render(requests, "html/start.html")

@login_required
def profile(requests):
    if requests.method == 'POST':
        form1 = AddPassword(requests.POST)
        if form1.is_valid():
            sourse_name = form1.cleaned_data['sourse_name']
            link_to_site = form1.cleaned_data['link_to_site']
            user_login = form1.cleaned_data['user_login']
            user_password = form1.cleaned_data['user_password']
            password_creation_date=timezone.now()
            user=requests.user
            submit=Passwords(
                sourse_name=sourse_name,
                link_to_site=link_to_site,
                user_login=user_login,
                user_password=user_password,
                user=user,
                password_creation_date=password_creation_date,
            )
            submit.save()
            messages.success(requests, f'Password have been created!')
            return redirect('loged_in')
    else:
        form1 = AddPassword()
    current_user = requests.user
    passwords=Passwords.objects.filter(user=current_user).order_by('-password_creation_date')
    data={
        'form1':form1,
        'passwords': passwords,
    }
    return render(requests, "html/logined.html", data)




def example(requests):
    user = User.objects.get(username='example')
    passwords = user.passwords_set.order_by('-password_creation_date')
    return render(requests, "html/example.html", {'passwords': passwords})


def register(requests):
    if requests.method == 'POST':
        form=UserRegisterForm(requests.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(requests, f'{username} account created! You are now able log in.')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(requests, 'html/register.html', {'form': form})

@login_required
def user_update(requests):
    if requests.method == 'POST':
        form=UserUpdateForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('loged_in')
    form=UserUpdateForm(instance=requests.user)
    return render(requests, "html/user_update.html", {'form':form})


class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model=Passwords
    template_name='html/passwords_detail.html'
    def test_func(self):
        password = self.get_object()
        if self.request.user == password.user:
            return True
        return False
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Passwords
    template_name='html/pass_update.html'
    fields = ['sourse_name', 'link_to_site', 'user_login', 'user_password', ]
    labels = {
           'sourse_name': 'Sourse Name',
            'link_to_site': 'Link To Source',
            'user_login': 'Login',
            'user_password': 'Password'
        }
    success_url='/profile/'
    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        password = self.get_object()
        if self.request.user == password.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Passwords
    template_name='html/passwords_delete.html'
    success_url='/profile/'
    def test_func(self):
        password = self.get_object()
        if self.request.user == password.user:
            return True
        return False



# переходы по внешним ссылкам
# имена лейблов
# генерация пароля
# шифрование

# сервер

# выезжающее окно
# главная страница



