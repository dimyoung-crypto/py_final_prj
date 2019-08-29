import django.db


class Project(django.db.models.Model):
    title = django.db.models.CharField(max_length=100)
    description = django.db.models.TextField()
    technology = django.db.models.CharField(max_length=20)
    image = django.db.models.FilePathField(path="/img")
