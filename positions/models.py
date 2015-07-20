# coding: utf-8

# This file is part of memopol.
#
# memopol is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# memopol is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with django-representatives.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>

from django.db import models
from django.template.defaultfilters import truncatewords

from constance import config

from legislature.models import MemopolRepresentative
from votes.models import MemopolDossier


class PositionManager(models.Manager):
    """A simple model manager for querying published Positions"""

    # https://docs.djangoproject.com/en/1.8/topics/db/managers/#using-managers-for-related-object-access
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(published=True, **kwargs)


class Position(models.Model):
    representative = models.ForeignKey(MemopolRepresentative, related_name='positions')
    dossier = models.ForeignKey(MemopolDossier, null=True, blank=True)
    datetime = models.DateField()
    text = models.TextField()
    link = models.URLField()
    published = models.BooleanField(default=False)

    # Adds our custom manager
    objects = PositionManager()


    def save(self, *args, **kwargs):
        """ Set published to default value and save the model"""
        self.published = config.POSITION_PUBLISHED
        super(Position, self).save(*args, **kwargs)

    @property
    def short_text(self):
        return truncatewords(self.text, 5)

    def publish(self):
        self.published = True

    def unpublish(self):
        self.published = False
