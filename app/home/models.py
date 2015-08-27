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

#TODO delete foreign key
EDUCATION_CHOICES = (
    ('Doctorat', 'Doctorat'),
    ('Maitrise', 'Maitrise'),
    ('Baccalaureat', 'Baccalaureat'),
)

#Education level
class Education(models.Model):
    class Meta:
        verbose_name_plural = _('Education')

    education = models.CharField(max_length=200, verbose_name=_('Education level'))
    def __unicode__(self):
        return self.education

#Areas of expertise
class Expertise(models.Model):
    class Meta:
        verbose_name_plural = _('Expertise')

    expertise = models.CharField(max_length=200, verbose_name=_('Area of expertise'))

    def __unicode__(self):
        return self.expertise

#User, we can't extends auth_user without auxiliar conflits
class UserProfile(models.Model):
    class Meta:
        ordering = ['user__last_name']

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name="profile", verbose_name=_('User'))
    userProfile_id = models.AutoField(primary_key=True, verbose_name=_('Identifiant'))

    # The additional attributes we wish to include.
    phone = models.CharField(max_length=10,verbose_name=_('Phone'),blank=True)
    website = models.URLField(blank=True,verbose_name=_('Web site'))
    picture = models.ImageField(upload_to='user_profile', blank=True,verbose_name=_('Picture'))

    facebook = models.URLField(blank=True, null=True, verbose_name=_('Facebook'))
    twitter = models.URLField(blank=True, null=True, verbose_name=_('Twitter'))
    googlePlus = models.URLField(blank=True, null=True, verbose_name=_('Google+'))
    linkedIn = models.URLField(blank=True, null=True, verbose_name=_('linkedIn'))

    def __unicode__(self):
        return self.user.username

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.allow_tags = True

class FloorPlan(models.Model):
    title = models.CharField(max_length=100,verbose_name=_('Title'))
    image = models.ImageField(upload_to='floor_plan', verbose_name=_('Image'))

    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    image_thumb.allow_tags = True








