from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
## Create your models here.
#class Poll(models.Model):
    #question = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    #def __unicode__(self):  # Python 3: def __str__(self):
        #return self.question
    #def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class Choice(models.Model):
    #poll = models.ForeignKey(Poll)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    #def __unicode__(self):  # Python 3: def __str__(self):
        #return self.choice_text


class Rider(models.Model):
    
    #current_post = models.ForeignKey(Post)

    #dummy = models.IntegerField(default=0)
    #username = models.CharField(max_length=200, unique=True)
    user = models.OneToOneField(User)
    #name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    #email = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    car_number = models.CharField(max_length=20, default=None)
    
    #path to image
    image = models.CharField(max_length=300, default="http://1.gravatar.com/avatar/7381ac88cc1a7fb5d0756e9698bf9b14?s=1024&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D1024&r=G")
    
    #1 - unverified
    #any other number = verification code
    verified = models.CharField(max_length=5)
    
    #0 - PAN
    #1 - Driving License
    #2 - Voter Card
    auth_type = models.CharField(max_length="20", default="None")
    auth_token = models.CharField(max_length=50, default = " ")
    
    
    #user_rating = models.IntegerField(default=5)
    neg_flags = models.IntegerField(default=0)
    
    #for reset_password
    reset_pass = models.CharField(default="",max_length=32)
    
    def __unicode__(self):
        return self.user.username


class Post(models.Model):
    
    owner = models.ForeignKey(Rider, null=False, related_name='owner')
    
    car_number = models.CharField(max_length=20, default=None)
    total_seats = models.IntegerField(default=1)
    phone = models.IntegerField(max_length=10)
    fro = models.CharField(max_length=200)
    to = models.CharField(max_length=200)
    date_time = models.DateTimeField('date_time',default=timezone.now())
    
    #0 - No
    #1 - Yes
    ac = models.IntegerField(default=0)
    autoaccept = models.IntegerField(default=0)
    
    #0 - Both
    #1 - Women only
    #2 - Men only
    men_women = models.IntegerField(default=0)
    
    
    #0 - available to all
    #1 - available to only friends
    available_to = models.IntegerField(default=0)
    
    cost = models.IntegerField(default=0)
    
    #0 - Doesn't want notifications
    #1 - Wants Notifications
    sms_noti = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.owner.user.username
    

class Reserved(models.Model):
    
    #Change primary key to combination of everything to prevent duplicates.
    
    post = models.ForeignKey(Post)
    reserver = models.ForeignKey(Rider)
    #0 - pending
    #1 - accepted
    status = models.IntegerField(default=0)
    
class Message(models.Model):
    
    #Change primary key to combination of everything to prevent duplicates.
    
    sender = models.ForeignKey(Rider, related_name = 'sender')
    receiver = models.ForeignKey(Rider, related_name = 'receiver')
    message = models.CharField(max_length=200)
    date_time = models.DateTimeField('date_time',default = timezone.now())
    
    
    #The next two variables denote whether the message is present in the sender's and receiver's mailboxes or not.
    #2 -> read: Not implemented yet
    #1 -> present
    #0 -> The user has deleted.
    #As soon as both become 0, the message will be deleted from the database.
    smailbox = models.IntegerField(default=1)
    rmailbox = models.IntegerField(default=1)
    
    
#Here there also exists another table called 'User', provided by Django. It has username, email and password attributes.


#Temp check form
class UploadFileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    #image = forms.FileField()