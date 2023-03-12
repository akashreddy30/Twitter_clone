from django.contrib import admin
from tweets.models import User
from tweets.models import Tweet
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name"]
class TweetAdmin(admin.ModelAdmin):
    list_display = ["username","content"]
admin.site.register(User,UserAdmin)
admin.site.register(Tweet,TweetAdmin)