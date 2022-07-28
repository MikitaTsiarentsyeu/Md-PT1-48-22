from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Writer(models.Model):
    """Писатель и автор"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="writers/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('writer_detail', kwargs={"slug": self.name})

 
    class Meta:
        verbose_name = "Писатель и автор"
        verbose_name_plural = "Писатель и автор"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Book(models.Model):
    """Книга"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="books/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2022)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Writer, verbose_name="писатель", related_name="book_director")
    writers = models.ManyToManyField(Writer, verbose_name="автор", related_name="book_author")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)



    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    book = models.ForeignKey(Book, verbose_name="книга", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"