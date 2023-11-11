from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Group)
admin.site.register(PersonalMsgs)
admin.site.register(Story)
admin.site.register(GrpMsg)