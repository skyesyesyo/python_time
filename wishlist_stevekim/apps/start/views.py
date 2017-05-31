# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.db.models import Count

from .models import User, Item, Like, UserManager

from django.contrib import messages

import bcrypt

# Create your views here.

def index(request):

	return render(request, 'start/index.html')

def validate(request):
	# This what what are you getting from request.POST
	# print '*' * 99
	# print request.POST
	# print '*' * 99

	if request.method == 'POST':
		# POST need to be in CAP!
		errors = User.objects.validate(request.POST)
		# success = User.objects.validate(request.POST['username'])
		if errors:
			for error in errors:
				messages.error(request, error)
		else:
			# Validation pass!
			messages.success(request, 'The user name you entered ({}) is valid! Thanks you!'.format(request.POST['username']))
			# Let's hash & salt password!
			hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

			# Let's add user!  &hashed password
			User.objects.create(name=request.POST['name'], username=request.POST['username'], password=hashed_pass, date_hire=request.POST['date_hire'])

			return redirect('/dashboard')

		
	return redirect('/')

def login(request):
	if request.method == "POST":
		users = User.objects.filter(username=request.POST['username'])
		if users:
			user = users[0]
			hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), user.password.encode())
			if user.password == hashed_pass:
				messages.success(request, "You have logged in successfully!")
				request.session['logged_user'] = user.id
				return redirect('/dashboard')

		messages.error(request, "Invalid password")
	return redirect('/')



def dashboard(request):
	user_id = request.session.get('logged_user')
	if not user_id:
		return redirect('/')

	context = {
		"users" : User.objects.all(),
		"name" : User.objects.all()[0],
	}

	return render(request, 'start/dashboard.html', context)

def makeawish(request):
	

	return render(request, 'start/makeawish.html')

def additem(request):
	user_id = request.session.get('logged_user')
	if not user_id:
		return redirect('/')
	user = User.objects.get(pk=user_id)
	if request.method == 'POST':
		Item.objects.create(makeawish=request.POST['wish_item'], user=user)
		return redirect('/dashboard')

	return redirect('/wish_items/create/')

def wish_item(request, id):
	user_id = request.session.get('logged_user')
	if not user_id:
		return redirect('/')
	user = User.objects.get(pk=user_id)
	item = Item.objects.get(pk=id)

	check_wish = Like.objects.filter(user=user, makeawish=item)
		# if not check_wish:
		# 	Like.object.create(user=user, makeawish=item)

	return render(request, 'start/wish_item.html')

def logout(request):

	del request.session['logged_user']
	return redirect('/')