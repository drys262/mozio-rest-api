from django.contrib import admin
from .models import Provider, ServiceArea


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    pass
