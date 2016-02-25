# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import os
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from embed_video.admin import AdminVideoMixin
from embed_video.fields import EmbedVideoField

#TODO delete foreign key
EDUCATION_CHOICES = (
    ('Doctorat', 'Doctorat'),
    ('Maitrise', 'Maitrise'),
    ('Baccalaureat', 'Baccalaureat'),
)


class Education(models.Model):
    # Education level
    class Meta:
        verbose_name_plural = _('Education')

    education = models.CharField(max_length=200, verbose_name=_('Education level'))

    def __unicode__(self):
        return self.education


class Expertise(models.Model):
    # Areas of expertise
    class Meta:
        verbose_name_plural = _('Expertise')

    expertise = models.CharField(max_length=200, verbose_name=_('Area of expertise'))

    def __unicode__(self):
        return self.expertise


class UserProfile(models.Model):
    # User, we can't extends auth_user without auxiliar conflits
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

    def save(self, *args, **kwarg):
        if self.userProfile_id:
            origin = UserProfile.objects.get(userProfile_id=self.userProfile_id)
            if origin.picture != self.picture:
                self.picture.name = unicode(self.userProfile_id) + os.path.splitext(self.picture.name)[1]

        super(UserProfile, self).save(*args, **kwarg)

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.picture)
    image_thumb.allow_tags = True

    def isCentech(self):
        groups = self.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return True
        return False

    def isExecutive(self):
        groups = self.user.groups.values()
        for group in groups:
            if group['name'] == 'Executive':
                return True
        return False

    def isFounder(self):
        from app.founder.models import Founder
        try:
            return Founder.objects.get(user = self.user)
        except:
            return False

    def isMentor(self):
        from app.mentor.models import Mentor
        try:
            return Mentor.objects.get(user = self.user)
        except:
            return False


# Deprecated : Use classes Rent classes instead
class FloorPlan(models.Model):
    title = models.CharField(max_length=100,verbose_name=_('Title'))
    image = models.ImageField(upload_to='floor_plan', verbose_name=_('Image'))

    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    image_thumb.allow_tags = True


class RoomType(models.Model):
    # Data
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.CharField(blank=True, max_length="100", verbose_name=_('Description'))
    is_rental = models.BooleanField(default=False, verbose_name=_('Is rental'))


class Room(models.Model):
    # Data
    from app.company.models import Company
    companies = models.ManyToManyField(
        Company,
        through='Rent',
        through_fields=('room', 'company'),
        verbose_name=_('Rented by')
    )
    type = models.ForeignKey(RoomType, verbose_name=_('Type'))

    code = models.CharField(blank=True, max_length=10, verbose_name=_('Code'))
    static_label = models.CharField(blank=True, max_length=100, verbose_name=_('Label'))

    coords = models.CommaSeparatedIntegerField(max_length=2000, verbose_name=_('Coordinates'))
    text_coords = models.CommaSeparatedIntegerField(
        null=True,
        max_length=50,
        verbose_name=_('Text area coordinates'))

    def is_rental(self):
        return self.type.is_rental

    def get_owner_name(self):
        owners = Rent.objects.filter(room=self.pk).order_by('-date_end')
        if len(owners) > 0:
            end_date = datetime.datetime.combine(owners[0].date_end, datetime.time.min)

            if end_date > datetime.datetime.now():
                return owners[0].company.name
            else:
                return False
        else:
            return False


class Rent(models.Model):
    from app.company.models import Company

    # Identifiers
    room = models.ForeignKey(Room, verbose_name=_('Room'))
    company = models.ForeignKey(Company, verbose_name=_('Company'))

    # Data
    date_start = models.DateField(verbose_name=_('Start date'))
    date_end = models.DateField(verbose_name=_('End date'))








