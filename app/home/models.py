# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from embed_video.admin import AdminVideoMixin
from embed_video.fields import EmbedVideoField
from django.utils import timezone

#Education level
class Education(models.Model):
    class Meta:
        verbose_name_plural = _('Education')

    education = models.CharField(max_length=200)
    def __str__(self):
        return self.education

#Areas of expertise
class Expertise(models.Model):
    class Meta:
        verbose_name_plural = _('Expertise')

    expertise = models.CharField(max_length=200)

    def __str__(self):
        return self.expertise

#User, we can't extends auth_user without auxiliar conflits
class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name="profile")
    userProfile_id = models.AutoField(primary_key=True)

    # The additional attributes we wish to include.
    phone = models.CharField(max_length=10,verbose_name=_('phone'),blank=True)
    website = models.URLField(blank=True,verbose_name=_('web site'))
    picture = models.ImageField(upload_to='user_profile', blank=True,verbose_name=_('personal photograph'))

    def __str__(self):
        return self.user.username

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.allow_tags = True












