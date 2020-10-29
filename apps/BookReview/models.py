from __future__ import unicode_literals
from django.db import models
from django import forms
# for regular expressions 
import re 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# WALLUSERMANAGER FOR VALIDATION
class WallUserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['Enter a first name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['Enter a last name'] = "Last name must be at least 2 characters"
        if not (postData['first_name']).isalpha() or not (postData['last_name']).isalpha():
            errors['Name only include letters'] = "Name only include letters"
        
        if not (re.search(regex,postData['email'])):  
              errors['Invalid email'] = "Invalid email address"
        if len(postData['email']) < 1:
            errors['Add your email'] = "Add your email"
        if len(postData['password']) < 8:
            errors['Password must be at least 8 characters'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm-password']:
            errors['Passwords don''t match'] = "Password don''t match"
        
        return errors


class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password_hash = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WallUserManager()

    def __str__(self):
        return ('first_name' + self.first_name + ', last_name = ' + self.last_name + ', email = ' + self.email)


class Book(models.Model):
    author = models.CharField(max_length = 255, null=True, blank=True)
    title = models.CharField(max_length = 255)
    submitted_by = models.ForeignKey(User, related_name="books_submitted")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return ("book = " + self.title)

class Review(models.Model):
    user_review = models.ForeignKey(User, related_name= "userreviews")
    books_review = models.ForeignKey(Book, related_name ="bookreviews")   
    review = models.TextField(null = True, blank=True)
    rating = models.CharField(max_length = 5, null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return ("review = " + self.review)


