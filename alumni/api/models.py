from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

from room.models import *

# Accounts
class Account(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # General
    profilePicture = models.ImageField('Profile Picture', null=True)
    firstName = models.CharField('First Name', max_length=255, null=True)
    lastName = models.CharField('Last Name', max_length=255, null=True)
    dateOfBirth = models.DateField("Date of Birth", null=True)
    age = models.IntegerField("Age of Alumni",default=0, null=True)

    # Contact
    mobileNumber = models.CharField('Mobile Number', max_length=13, null=True)
    emailID = models.EmailField('Email Address', null=True)

    
    role = models.CharField('Role', max_length=255, null=True)
    location = models.CharField('Location', max_length=255, null=True)

    # Followers
    followers = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return str(self.id) + " | " + str(self.user.username)

    
class Student(models.Model):
    
    BRANCH = (
        ('Computer Science and Engineering', 'Computer Science and Engineering'),
    )
    
    SECTION = (
        ('None', 'None'),
        ('Alpha', 'Alpha'),
        ('Beta', 'Beta'),
        ('Gamma', 'Gamma'),
    )

    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    branch = models.CharField('Branch', choices=BRANCH, max_length=100, null=True)
    section = models.CharField('Section', choices=SECTION, max_length=100, null=True)
    batch = models.CharField('Batch', max_length=100, null=True)

    def __str__(self):
        return (self.id)


class Faculty(models.Model):

    DEPARTMENT = (
        ('Computer Science and Engineering', 'Computer Science and Engineering'),
    )
    
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    startYear = models.CharField('Start Year', max_length=4, null=True)
    department = models.CharField('Department', choices=DEPARTMENT, max_length=100, null=True)

    def __str__(self):
        return (self.id)
    

# Content
class Like(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.id) + " | " + str(self.account.id) + " | " + str(self.date_created))
    
class Comment(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    text = models.CharField('Text', max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField('Likes', default=0)

    def __str__(self):
        return (str(self.id) + " | " + self.text + " | " + str(self.date_created))
    

class Post(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    image = models.ImageField('Image', null=True)
    caption = models.CharField('Caption', max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(Like, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return (str(self.id) + " | " + self.caption + " | " + str(self.date_created))
    

class Job(models.Model):

    def __str__(self):
        return (self.id)