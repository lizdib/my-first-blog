from django.db import models
from django.utils import timezone

class Reply(models.Model):
    title = models.CharField(max_length=20, default='')
    name_of_inhabitant = models.CharField(max_length=100, blank=False, primary_key=True, serialize=False)
    #ForeignKey('auth.User', on_delete=models.CASCADE)
    name_of_organisation = models.CharField(max_length=30, blank=False)
    result = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Request(models.Model):
    title = models.CharField(max_length=20, default='')
    name_of_inhabitant = models.CharField(max_length=100, blank=False, primary_key=True, serialize=False)
    #ForeignKey('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Reply_register(models.Model):
    title = models.CharField(max_length=20, default='')
    reply_number = models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID', blank=False)
    name_of_inhabitant = models.CharField(max_length=100, blank=False)
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
    request_number = models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID', blank=False)
    name_of_inhabitant = models.CharField(max_length=100, blank=False)
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
