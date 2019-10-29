from django.contrib import admin

from .models import Profile, Business, Neighbourhood, EmergencyContact, Post

admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(EmergencyContact)
admin.site.register(Post)
