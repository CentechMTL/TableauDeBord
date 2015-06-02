from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from app.home.models import UserProfile,Expertise,Education

#Founder
class Founder(UserProfile):
    education = models.ForeignKey(Education,verbose_name=_('Education level'),blank=True, null=True)
    expertise = models.ManyToManyField(Expertise,verbose_name=_('Areas of expertise'),blank=True)
    equity = models.FloatField(default=0,blank=True)
    about = models.CharField(max_length=2000,verbose_name=_('about'),blank=True);

    def __str__(self):
        return self.user.username
