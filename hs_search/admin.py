from django.contrib import admin
from models import *

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Note)
admin.site.register(Section)
admin.site.register(Chapter)
admin.site.register(Article)


class HSCodeAdmin(admin.ModelAdmin):
    list_display = ['hs','desc','article']

admin.site.register(hscode,HSCodeAdmin)
