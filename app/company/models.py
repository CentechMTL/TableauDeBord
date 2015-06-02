from django.db import models
from datetime import datetime
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from django.utils.translation import ugettext_lazy as _
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.core.urlresolvers import reverse
from django import forms

#Status of a company in the Centech (ex: emergence)
class CompanyStatus(models.Model):
    class Meta:
        verbose_name_plural = _('Company Status')

    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

#Companies
class Company(models.Model):
    class Meta:
        verbose_name_plural = _('Companies')

    #General information
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo',blank=True)
    url = models.URLField(blank=True)
    video = EmbedVideoField(blank=True)
    description = models.TextField(blank=True,max_length=2000)
    companyStatus = models.ForeignKey(CompanyStatus,verbose_name=_('Phase'))

    #List of founders
    founders = models.ManyToManyField(Founder,blank=True)
    #List of mentors
    mentors = models.ManyToManyField(Mentor,blank=True)

    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

    def save(self):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Company, self).save()

    def getMentors(self):
        return self.mentors

    def getFounders(self):
        return self.founders

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.logo)
    image_thumb.allow_tags = True

#Presence of companies
class Presence(models.Model):
    class Meta:
        verbose_name_plural = _('Presences')

    #List of company
    company = models.ManyToManyField(Company,blank=True)
    #Date of the meeting
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('company:presence_list')