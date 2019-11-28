from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# class Users(models.Model):
#     user_name=models.CharField("user_name", max_length=200)
#     user_unique_pass=models.CharField("user_unique_pass", max_length=200)
#     user_to_login_pass=models.CharField("user_to_login_pass", max_length=200)

#     def __str__(self):
#         return self.user_name

class Passwords(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,)
    sourse_name=models.CharField("sourse_name", max_length=200)#(тип поля, соотвецтвует Varchar)
    user_login=models.CharField("user_login", max_length=200)
    user_password=models.CharField("user_passord", max_length=200)
    password_creation_date=models.DateTimeField("password_creation_date", null=True)
    link_to_site=models.CharField("link_to_site", max_length=200)
    count_of_search=models.IntegerField("count_of_search", default=0)
    count_of_copy=models.IntegerField("count_of_copy", default=0)

    def __str__(self):
        return self.sourse_name

    def get_absolute_url(self):
        return reverse('password_detail', kwargs={'pk': self.pk})

    def aller_pass_update(self):
        return self.password_creation_date <= (timezone.now() - datetime.timedelta(days=30))
            # возвращает нет если прошло больше 60 днейS

