# coding: utf-8

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RoomType(models.Model):
    # Data
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name')
    )
    bg_color = models.CharField(
        default="#FFFFFF",
        max_length=7,
        verbose_name=_('Background color'),
        help_text=_("Please use the following format: #FFFFFF")
    )
    alt_bg_color = models.CharField(
        blank=True,
        max_length=7,
        verbose_name=_('Alternative background color'),
        help_text=_("Used for type state change (e.g. occupied rental)"
                    "<br />Please use the following format: #FFFFFF")
    )
    description = models.TextField(
        blank=True,
        max_length=500,
        verbose_name=_('Description')
    )
    is_rental = models.BooleanField(
        default=False,
        verbose_name=_('Is rental')
    )

    def __unicode__(self):
        return self.name


class Room(models.Model):
    # Data
    type = models.ForeignKey(RoomType, verbose_name=_('Type'))

    """
    CommaSeparatedIntegerField:
        Stores a string of integers separated by commas (e.g. "0,0,100,200")
        Therefore, max_length refers to the string length and not list capacity
        So to support the list [1,2,3,4] the lowest max_length would be 7
            (no spaces allowed, brackets are excluded)

    Coordinates syntax:
        The system expects a list of integers to be interpreted as
            a list of points
        See HTML map tag for reference
    """
    coords = models.CommaSeparatedIntegerField(
        max_length=2000,
        verbose_name=_('Coordinates'),
        help_text=_(
            "For a rectangle, please use the following format: "
            "<em>x1,y1,x2,y2</em>.<br>"
            "For a polygon, please use the following format: "
            "<em>x1,y1,...,xn,yn</em>."
        )
    )

    code = models.CharField(
        max_length=10,
        verbose_name=_('Code')
    )
    static_label = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('Label'),
        help_text=_(
            "<b>Warning:</b> Will be overwritten by rental owner, if any."
        )
    )

    text_coords = models.CommaSeparatedIntegerField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name=_('Text area coordinates'),
        help_text=_(
            "Area where the label should be displayed "
            "(defaults to room coordinates)<br>"
            "Please use the following format: "
            "<em>x1,y1,x2,y2</em>. <b>Rectangle only!</b>"
        )
    )

    def __unicode__(self):
        if self.static_label:
            return u"{code} - {label}".format(
                code=self.code,
                label=self.static_label
            )
        else:
            return self.code

    def is_rental(self):
        return self.type.is_rental

    def get_owner_name(self):
        """
        :return:
            The company owner's name if the room type has the is_rental flag
            Otherwise returns boolean False
        """
        if self.is_rental():
            owner_result = self.rentals.filter(
                date_end__gte=datetime.date.today(),
                date_start__lte=datetime.date.today()
            ).first()

            if owner_result:
                return owner_result.company.name
            else:
                return False
        else:
            return False


class Rent(models.Model):
    # Identifiers
    room = models.ForeignKey(
        Room, verbose_name=_('Room'),
        related_name='rentals'
    )
    company = models.ForeignKey(
        'company.Company', verbose_name=_('Company'),
        related_name='rentals'
    )

    # Data
    date_start = models.DateField(verbose_name=_('Start date'))
    date_end = models.DateField(verbose_name=_('End date'))

    def __unicode__(self):
        return "_".join((
            str(self.room),
            str(self.date_start),
            str(self.date_end)
        ))
