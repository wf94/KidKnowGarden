# Register your models here.
from django.contrib import admin
from kidKnowGarden.models import *

admin.site.register(
    Rooms,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(ContestScore)
admin.site.register(Room_Profile)
admin.site.register(CorrectAnswer)
admin.site.register(LearnHistory)