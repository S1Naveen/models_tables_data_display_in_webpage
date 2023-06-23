from django.db import models

# Create your models here.
class Topic_view(models.Model):
    topic_name=models.CharField(max_length=50)
    id=models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.topic_name

class Webpage_view(models.Model):
    topic_name=models.ForeignKey(Topic_view,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()

    def __str__(self) -> str:
        return self.name



class Access_view(models.Model):
    name=models.ForeignKey(Webpage_view,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.author