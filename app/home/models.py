# coding: utf-8

import os

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# TODO delete foreign key
EDUCATION_CHOICES = (
    ('Doctorat', 'Doctorat'),
    ('Maitrise', 'Maitrise'),
    ('Baccalaureat', 'Baccalaureat'),
)


class Education(models.Model):
    # Education level
    class Meta:
        verbose_name_plural = _('Education')

    education = models.CharField(
        max_length=200,
        verbose_name=_('Education level')
    )

    def __unicode__(self):
        return self.education


class Expertise(models.Model):
    # Areas of expertise
    class Meta:
        verbose_name_plural = _('Expertise')

    expertise = models.CharField(
        max_length=200,
        verbose_name=_('Area of expertise')
    )

    def __unicode__(self):
        return self.expertise


class UserProfile(models.Model):
    # User, we can't extends auth_user without auxiliary conflicts
    class Meta:
        ordering = ['user__last_name']

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(
        User,
        related_name="profile",
        verbose_name=_('User')
    )
    userProfile_id = models.AutoField(
        primary_key=True,
        verbose_name=_('Identifiant')
    )

    # The additional attributes we wish to include.
    phone = models.CharField(
        max_length=10,
        verbose_name=_('Phone'),
        blank=True
    )
    website = models.URLField(
        blank=True,
        verbose_name=_('Web site')
    )
    picture = models.ImageField(
        upload_to='user_profile',
        blank=True,
        verbose_name=_('Picture')
    )

    facebook = models.URLField(
        blank=True,
        null=True, verbose_name=_('Facebook')
    )
    twitter = models.URLField(
        blank=True,
        null=True, verbose_name=_('Twitter')
    )
    googlePlus = models.URLField(
        blank=True,
        null=True, verbose_name=_('Google+')
    )
    linkedIn = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('linkedIn')
    )

    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwarg):
        if self.userProfile_id:
            origin = UserProfile.objects.get(
                userProfile_id=self.userProfile_id
            )
            if origin.picture != self.picture:
                self.picture.name = unicode(self.userProfile_id) + \
                                    os.path.splitext(self.picture.name)[1]

        super(UserProfile, self).save(*args, **kwarg)

    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % \
               self.picture

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
            return Founder.objects.get(user=self.user)
        except:
            return False

    def isMentor(self):
        from app.mentor.models import Mentor
        try:
            return Mentor.objects.get(user=self.user)
        except:
            return False
