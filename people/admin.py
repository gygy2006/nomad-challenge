from django.contrib import admin
from people.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

  list_display = (
    "name",
    "kind",
    "photo"
  )
  list_filter = ("kind",)