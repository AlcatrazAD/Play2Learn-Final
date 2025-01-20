from django.contrib import admin

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['submission', 'created']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created')

        return ()
