from django.db import models
from django.utils import timezone

class Reply(models.Model):
    title = models.CharField(max_length=200, default='')
    name_of_inhabitant = models.CharField(max_length=200, blank=False)
    #ForeignKey('auth.User', on_delete=models.CASCADE)
    name_of_organisation = models.CharField(max_length=200, blank=False)
    result = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Request(models.Model):
    title1 = models.CharField(max_length=200, default='')
    name_of_inhabitant1 = models.CharField(max_length=200, blank=False)
    #ForeignKey('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title1
