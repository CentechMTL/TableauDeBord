# coding: utf-8

from django.db import models
from datetime import datetime
import time
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

    status = models.CharField(max_length=50, verbose_name=_('Name'))

    def __str__(self):
        return self.status

#Companies
class Company(models.Model):
    class Meta:
        verbose_name_plural = _('Companies')

    #General information
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    logo = models.ImageField(upload_to='logo',blank=True, verbose_name=_('Logo'))
    url = models.URLField(blank=True, verbose_name=_('URL'))
    video = EmbedVideoField(blank=True, verbose_name=_('Video'))
    description = models.TextField(blank=True,max_length=2000, verbose_name=_('Description'))
    companyStatus = models.ForeignKey(CompanyStatus,verbose_name=_('Status'))

    #List of founders
    founders = models.ManyToManyField(Founder,blank=True, verbose_name=_('Founders'), related_name = "company")
    #List of mentors
    mentors = models.ManyToManyField(Mentor,blank=True, verbose_name=_('Mentors'), related_name = "company")

    facebook = models.URLField(blank=True, null=True, verbose_name=_('Facebook'))
    twitter = models.URLField(blank=True, null=True, verbose_name=_('Twitter'))
    googlePlus = models.URLField(blank=True, null=True, verbose_name=_('Google+'))
    linkedIn = models.URLField(blank=True, null=True, verbose_name=_('linkedIn'))

    incubated_on = models.DateField(blank=True, null=True)
    endOfIncubation = models.DateField(blank=True, null=True)

    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwarg):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Company, self).save(*args, **kwarg)

    def get_users(self):
        users = []

        founders =  self.founders.all()
        for founder in founders:
            users.append(founder.user)

        mentors = self.mentors.all()
        for mentor in mentors:
            users.append(mentor.user)

        return users

    def get_last_irl(self):
        irls =  self.KPIs.filter(type="IRL").order_by("-period_start")
        if irls:
            return irls[0]
        else:
            return None

    def get_last_trl(self):
        trls =  self.KPIs.filter(type="TRL").order_by("-period_start")
        if trls:
            return trls[0]
        else:
            return None

    def get_last_experiment(self):
        experiments =  self.experiments.order_by("-dateFinish")
        if experiments:
            return experiments[0]
        else:
            return None

    def get_percentage_incubation_time(self):
        if self.incubated_on and self.endOfIncubation:
            now = datetime.date(datetime.today())
            delta_days = (now - self.incubated_on).days
            timeOfIncubation = (self.endOfIncubation - self.incubated_on).days
            percentage = int(round(((float(delta_days))/timeOfIncubation)*100, 0))
            if percentage > 100:
                return 100
            else:
                return percentage
        else:
            return None

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.logo)
    image_thumb.allow_tags = True

#Presence of companies
class Presence(models.Model):
    class Meta:
        verbose_name_plural = _('Presences')

    #List of company
    company = models.ManyToManyField(Company,blank=True, verbose_name=_('Companies'))
    #Date of the meeting
    date = models.DateTimeField(blank=True, verbose_name=_('Date'))

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('company:presence_list')