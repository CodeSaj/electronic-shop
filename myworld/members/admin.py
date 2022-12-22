from django.contrib import admin
from .models import Members

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("username", "password", "email",)

admin.site.register(Members, MemberAdmin)