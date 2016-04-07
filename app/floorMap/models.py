# coding: utf-8

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RoomType(models.Model):
    # Data
    name = models.CharField(
        max_length=100,
        verbose_name=_(u'Name')
    )
    bg_color = models.CharField(
        default="#FFFFFF",
        max_length=7,
        verbose_name=_(u'Background color'),
        help_text=_(
            u"Please use the following format: {format}"
        ).format(format="#FFFFFF")
    )
    alt_bg_color = models.CharField(
        blank=True,
        max_length=7,
        verbose_name=_(u'Alternative background color'),
        help_text=u"{help_alt_bg}<br>{help_bg_color}".format(
            help_alt_bg=_(
                u"Used for type state change (e.g. occupied rental)"
            ),
            help_bg_color=_(
                u"Please use the following format: {format}"
            ).format(format="#FFFFFF")
        )
    )
    description = models.TextField(
        blank=True,
        max_length=500,
        verbose_name=_(u'Description')
    )
    is_rental = models.BooleanField(
        default=False,
        verbose_name=_(u'Is rental')
    )

    def __unicode__(self):
        return self.name


class Room(models.Model):
    # Data
    type = models.ForeignKey(RoomType, verbose_name=_(u'Type'))

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
        verbose_name=_(u'Coordinates'),
        help_text=u"<b>{shape_rect}:</b> {format_rect}<br />"
                  u"<b>{shape_poly}:</b> {format_poly}".format(
            shape_rect=_(u"Rectangle"),
            shape_poly=_(u"Polygon"),
            format_rect=_(
                u"Please use the following format: {format}"
            ).format(format=u"<em>x1,y1,x2,y2</em>"),
            format_poly=_(
                u"Please use the following format: {format}"
            ).format(format=u"<em>x1,y1,...,xn,yn</em>")
        )
    )

    code = models.CharField(
        max_length=10,
        verbose_name=_(u'Room code')
    )
    static_label = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_(u'Label'),
        help_text=u"<b>{warning}:</b> {warning_message}".format(
            warning=_(u"Warning"),
            warning_message=_(u"Will be overwritten by rental owner name.")
        )
    )

    text_coords = models.CommaSeparatedIntegerField(
        blank=True,
        null=True,
        max_length=50,
        verbose_name=_(u'Text area coordinates'),
        help_text=u"{description}<br />{format}. <b>{restriction}</b>".format(
            description=_(u"Area where the label will be displayed "
                          u"(defaults to room coordinates)"),
            format=u"<em>x1,y1,x2,y2</em>",
            restriction=_(u"Rectangle only!")
        )
    )

    surface_size = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_(u"Surface size"),
        help_text=_(u"Value in ft².")
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

    def get_active_rental(self):
        """
        :return:
            The current active rental occupied in this room
            Returns false if none,
                or if room type doesn't have the is_rental flag
        """
        if self.is_rental():
            return self.rentals.filter(
                date_end__gte=datetime.date.today(),
                date_start__lte=datetime.date.today()
            ).first()
        else:
            return self.rentals.none()

    def get_upcoming_rentals(self):
        """
        :return:
            Returns upcoming rentals for this room
        """
        if self.is_rental():
            return self.rentals.filter(
                date_start__gt=datetime.date.today()
            )
        else:
            return self.rentals.none()

    def get_owner_name(self):
        """
        :return:
            The company owner's name if the room type has the is_rental flag
            Otherwise returns boolean False
        """
        active_rental = self.get_active_rental()

        if active_rental:
            return active_rental.company.name
        else:
            return ''


class Rent(models.Model):
    # Identifiers
    room = models.ForeignKey(
        Room, verbose_name=_(u'Room'),
        related_name='rentals'
    )
    company = models.ForeignKey(
        'company.Company', verbose_name=_(u'Company'),
        related_name='rentals'
    )

    # Data
    date_start = models.DateField(verbose_name=_(u'Start date'))
    date_end = models.DateField(verbose_name=_(u'End date'))

    def __unicode__(self):
        return "_".join((
            str(self.room),
            str(self.date_start),
            str(self.date_end)
        ))
