# coding: utf-8
from django import template
from django.contrib.humanize.templatetags.humanize import naturalday
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from representatives.models import Group, Mandate

register = template.Library()


@register.filter
def mandate_date(date, arg=None):
    if date.year == 9999:
        return 'present'
    else:
        return naturalday(date, arg)


@register.filter
def position_icon(position):
    if position == 'for':
        return mark_safe(
            '<i \
            aria-label="for" \
            class="fa fa-thumbs-up vote_positive" \
            title="for" \
            ></i>')
    elif position == 'against':
        return mark_safe(
            '<i \
            aria-label="against" \
            class="fa fa-thumbs-down vote_negative" \
            title="against" \
            ></i>')
    else:
        return mark_safe(
            '<i \
            aria-label="abstain" \
            class="fa fa-circle-o vote_abstain" \
            title="abstain" \
            ></i>')


@register.filter
def score_label(score):
    if score > 0:
        return mark_safe(
            '<span class="label label-success">{}</span>'.format(score))
    elif score < 0:
        return mark_safe(
            '<span class="label label-danger">{}</span>'.format(score))
    else:
        return mark_safe(
            '<span class="label label-default">{}</span>'.format(score))


@register.filter
def country_flag(country):
    return mark_safe(
        '<span class="flag-icon flag-icon-{code}"></span> {name}'.format(
            name=country.name,
            code=country.code.lower()))


@register.filter
def by_group_url(group):
    if isinstance(group, Mandate):
        group = group.group

    if not isinstance(group, Group):
        return ''

    kwargs = {'group_kind': group.kind}

    if group.abbreviation:
        kwargs['group'] = group.abbreviation
    else:
        kwargs['group'] = group.name

    return reverse(
        'positions:representative-list',
        kwargs=kwargs
    )
