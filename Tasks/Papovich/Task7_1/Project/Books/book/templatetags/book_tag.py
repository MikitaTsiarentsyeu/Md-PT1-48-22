from django import template
from book.models import Category, Book


register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()

@register.inclusion_tag('book/tags/last_book.html')
def get_last_book(count=5):
    book = Book.objects.order_by("id")[:count]
    return {"last_book": book}