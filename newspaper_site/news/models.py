from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

class ContributeForm(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    Explanation = models.TextField()
