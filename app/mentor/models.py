# coding: utf-8

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from app.home.models import UserProfile,Expertise
from app.founder.models import Founder

#Mentors
class Mentor(UserProfile):
    expertise = models.ManyToManyField(Expertise,verbose_name=_('Areas of expertise'))
    about = models.CharField(max_length=2000,blank=True,verbose_name=_('About'));

    def __str__(self):
        return self.user.username

    def get_queryset(self):
        return Mentor.objects.all()

    def save(self):
        if not self.pk:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Mentor, self).save()

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.allow_tags = True