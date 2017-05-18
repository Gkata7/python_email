from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
    def login(self,email):
        errors =[]
        if len(email) == 0:
            errors.append("Email is Required")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid Email")
        if len(errors) is not 0:
            return(False,errors)
        else:
            e = Email.objects.create(email=email)
            e.save()
            return(True, e)

    def delete(self,id):
        e = Email.objects.get(id=id)
        if not e:
            return(False, "NO email found with that ID")
        else:
            e.delete()
            return(True, "Email Deleted")

class Email(models.Model):
    email = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailManager()
