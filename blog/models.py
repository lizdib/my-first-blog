from django.db import models
from django.utils import timezone

class Reply(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID', blank=False)
    name_of_inhabitant = models.CharField(max_length=100, blank=False)
    result = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.id

class Request(models.Model):
    id = models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID', blank=False)
    name_of_inhabitant = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.id

class Reply_register(models.Model):
    title = models.CharField(max_length=20, default='')
    reply_number = models.CharField(max_length=20, primary_key=True, serialize=False, blank=False)
    name_of_inhabitant = models.ForeignKey(Reply)
    result = models.TextField()
    name_of_doer = models.CharField(max_length=100, blank=False)
    request_status = models.CharField(max_length=10, blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Request_register(models.Model):
    title = models.CharField(max_length=20, default='')
    request_number = models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID', blank=False)
    name_of_inhabitant = models.ForeignKey(Request)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    name_of_doer = models.CharField(max_length=100, blank=False)
    request_status = models.CharField(max_length=10, blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
