from Insta.models import Like
from django import template
register = template.Library()

@register.simple_tag
def has_user_liked_post(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fas fa-heart fa-2px show-color-heart"
    except:
        return "far fa-heart fa-2px"