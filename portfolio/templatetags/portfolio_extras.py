import re

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()

_ACCENT_RE = re.compile(r'\*\*(.+?)\*\*')


@register.filter
def accentuate(value):
    """
    Turns 'Building products layer by **layer**.' into HTML where the
    double-asterisk word is wrapped in <span class="accent">...</span>,
    so it renders with the theme's highlight color.
    """
    escaped = escape(value)
    replaced = _ACCENT_RE.sub(r'<span class="accent">\1</span>', escaped)
    return mark_safe(replaced)
