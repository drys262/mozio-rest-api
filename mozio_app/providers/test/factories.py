import factory

from providers.models import Provider, ServiceArea


class ProviderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Provider

    id = factory.Faker('uuid4')

    name = factory.Faker('name')
    phone_number = factory.Faker('phone_number')
    language = factory.Faker('language')
    email = factory.Faker('email')
    currency = factory.Faker('currency')


# class ServiceAreaFactory(factory.django.DjangoModelFactory):

#     class Meta:
#         model = ServiceArea

#     id = factory.Faker('uuid4')

#     provider = factory.Faker('name')
#     phone_number = factory.Faker('phone_number')
#     language = factory.Faker('language')
#     email = factory.Faker('email')
#     currency = factory.Faker('currency')
