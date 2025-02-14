from django.template import Library
from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_uploader_display(context, user):
    if context['user'] == user:
        return 'Vous'
    else:
        return user.username


@register.filter
def get_posted_at_display(posted_at):
    seconds_ago = (timezone.now() - posted_at).total_seconds()
    if seconds_ago <= HOUR:
        return f"Publié il y a {int(seconds_ago // MINUTE)} minutes."
    elif seconds_ago <= DAY:
        return f"Publié il y a {int(seconds_ago // HOUR)} heures."
    return f"Publié le {posted_at.strftime('%d/%m/%Y à %H:%M')}"


@register.filter
def rating_into_stars(value):
    """Converts a numeric rating (0-5) to a string of stars ⭐."""
    try:
        value = int(value)
        return "★" * value + "☆" * (5 - value)
    except ValueError:
        return "Note invalide"


@register.filter
def add_class(field, css_class):
    """Add a CSS class to a Django form field"""
    return field.as_widget(attrs={"class": css_class})
