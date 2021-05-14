from django.contrib import admin
from .models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):

    readonly_fields = ('created_date', 'update_date')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Manager").exists():
            # Hides 'created_date' and 'update_date' to users in group 'Manager'
            return ('key', 'name')
        else:
            return ('created_date', 'update_date')


admin.site.register(Link, LinkAdmin)
