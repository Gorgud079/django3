from django import template
from woman.models import *
from woman import constanta
register = template.Library()


@register.inclusion_tag('woman/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    w1 = Woman.objects.filter(cat_id=1)
    w2 = Woman.objects.filter(cat_id=2)
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected, 'wo': w1, 'wo2': w2 }


@register.inclusion_tag('woman/show_menu.html')
def show_menu():
    menu = constanta.menu
    return {'menu': menu}

