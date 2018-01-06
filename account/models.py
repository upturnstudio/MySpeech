from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User, AnonymousUser
from django.db.models.signals import post_save

from utils.db.fields.country import CountryField
from utils.db.fields.gender import GenderField

class UserInfo(models.Model):
    desc = models.CharField(max_length=300, default='')
    subs_on_dispatch = models.BooleanField(default=False)  # подписка на рассылку
    path_to_avatar = models.CharField(max_length=100, unique=True, default='')
    num_of_subs = ArrayField(models.CharField(max_length=16, unique=True), default=[])
    num_of_followers = ArrayField(models.CharField(max_length=16, unique=True), default=[])
    gender = GenderField(default='N')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=100)
    country = CountryField(default='EN')


"""
class PlayList(models.Model):
    #общие свойства для плейлиста и для аудио
    title = models.TextField()
    desc = models.TextField(blank=True)
    duratiosn = models.TimeField()
    date_create = models.DateField()
    path_to_picture = models.CharField(max_length=100, unique=True, blank=True)
    private = models.IntegerField(default=0) # 0 - для всех; 1 - для друзей(при привтном аккаунте отсутсвует); 2 - для себя
    list_likes = ArrayField(models.CharField(max_length=16, unique=True)) # списки лайков и списки добавялющих
    list_add = ArrayField(models.CharField(max_length=16, unique=True))
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    playlist_id = models.CharField(max_length=40, unique=True)


class Audio(models.Model):
    title = models.TextField()
    desc = models.TextField(blank=True)
    duration = models.TimeField()
    date_upload = models.DateField()
    path_to_picture = models.CharField(max_length=100, blank=True, unique=True)
    private = models.IntegerField(default=0) # 0 - для всех; 1 - для друзей(при привтном аккаунте отсутсвует); 2 - для себя
    list_likes = ArrayField(models.CharField(max_length=16, unique=True), blank=True) # списки лайков и списки добавялющих
    list_add = ArrayField(models.CharField(max_length=16, unique=True), blank=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    path_to_file = models.CharField(max_length=100, unique=True)
    audio_id = models.CharField(max_length=40, unique=True)

"""