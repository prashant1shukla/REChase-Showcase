from django import template
from sudoku import utils

register = template.Library()

prefilled = utils.prefilled


@register.filter(name='get_val')
def get_val(row, col):
    print(row, col)
    return prefilled.get('{}{}'.format(row, col))


@register.simple_tag(name='get_val_extra')
def get_val_extra(pref, row, col):
    x = pref.get('{}{}'.format(row, col))
    return x
