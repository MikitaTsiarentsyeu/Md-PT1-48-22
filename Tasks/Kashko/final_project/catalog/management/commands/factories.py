import factory
from factory.django import DjangoModelFactory, ImageField

from catalog.models import Category, City, Contact, Item


class CategoryFactory(DjangoModelFactory):

    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = factory.Faker('word')


class CityFactory(DjangoModelFactory):

    class Meta:
        model = City
        django_get_or_create = ('name',)

    name = factory.Faker('city')


class ContactFactory(DjangoModelFactory):

    class Meta:
        model = Contact
        django_get_or_create = (
            'email',
            'phone_number',
        )

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('numerify', text='+375#########')


class ItemFactory(DjangoModelFactory):

    class Meta:
        model = Item
        django_get_or_create = (
            'category',
            'who_found',
            'who_lost'
        )

    is_active = factory.Faker('boolean', chance_of_getting_true=80)
    name = factory.Faker('word')
    category = factory.SubFactory(CategoryFactory)
    type = factory.Faker('random_element', elements=('l', 'f'))
    description = factory.Faker("paragraph",
                                nb_sentences=5,
                                variable_nb_sentences=True)
    city = factory.SubFactory(CityFactory)
    who_found = factory.SubFactory(ContactFactory)
    who_lost = factory.SubFactory(ContactFactory)
    image = ImageField(from_path='catalog/management/commands/test_image.png',
                       width=1280,
                       height=1024)
