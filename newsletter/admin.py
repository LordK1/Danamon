from django.contrib import admin

# Register your models here.
from newsletter.forms import SignUpForm
from newsletter.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "timestamp", "updated"]
    form = SignUpForm

    # class Meta:
    #     model = SignUp


admin.site.register(SignUp, SignUpAdmin)
