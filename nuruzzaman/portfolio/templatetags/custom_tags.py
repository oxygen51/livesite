from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """Generate a range for the given value."""
    return range(value)

@register.simple_tag
def calculate_empty_stars(filled_stars, total_stars=5):
    """Calculate the empty stars needed to make up the total."""
    return range(total_stars - filled_stars)
