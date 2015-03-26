from django.contrib import admin
from blogspot.models import *
from django.template.defaultfilters import slugify
from unidecode import unidecode


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links = ('title',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(PostAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    prepopulated_fields = {'slug': (slugify(unidecode('title')),)}

admin.site.register(Post, PostAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
