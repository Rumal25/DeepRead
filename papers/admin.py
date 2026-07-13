from django.contrib import admin
from papers.models import Author, Paper, Topic, Citation, ReadingNote, Experiment

admin.site.register(Author)
admin.site.register(Paper)
admin.site.register(Topic)
admin.site.register(Citation)
admin.site.register(ReadingNote)
admin.site.register(Experiment)