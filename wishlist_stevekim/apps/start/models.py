# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserManager(models.Manager):
	def validate(self, post):
		username = post['username']
		password = post['password']
		passconf = post['passconf']
		errors = []
###
		name = post['name']
		date_hire = post['date_hire']
		if not name:
			errors.append('name field is required')
		if not date_hire:
			errors.append('date hire field is required')
###
		if not username:
			errors.append('username field is required')
		if not password:
			errors.append('password field is required')
		elif len(password) <8:
			errors.append('password must be at least 8 characters long')
		elif not password == passconf:
			errors.append('password and confirm password much match')


		##
		if len(name) <3:
			errors.append('name must be at least 3 characters long')
		##
		if len(username) <3:
			errors.append('username must be at least 3 characters long')

		return errors

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_hire = models.DateTimeField(auto_now = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class Item(models.Model):
	wish_item = models.CharField(max_length=100)
	user = models.ForeignKey("User")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# This is many to many table
class Like(models.Model):
	user = models.ForeignKey("User")
	wish_item = models.ForeignKey(Item)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)