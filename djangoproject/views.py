from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from djangoproject.models import Contact, Employees
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


# User Signup function
def userSignUp(request):
	if request.method == "POST":
		fms = SignUpForm(request.POST)
		if fms.is_valid():
			fms.save()
			messages.success(request, 'Signup successfully !!')
	else:
		fms = SignUpForm()
	
	return render(request, 'signup.html', {'forms' : fms})

# User Login funtion
def userlogin(request):
	if request.method == "POST":
		fms = LoginForm(request=request, data=request.POST)
		if fms.is_valid():
			uname = fms.cleaned_data['username']
			upass = fms.cleaned_data['password']
			user = authenticate(username=uname, password=upass)
			if user is not None:
				login(request, user)
				return redirect('/')
	else:
		fms = LoginForm()
	return render(request, 'userlogin.html', {'forms' : fms})

# User Logout function
def user_logout(request):
	logout(request)
	return redirect('/login')	

# Home function
def index(request):
	if not request.user.is_authenticated:
		return redirect('/login')

	return render(request, 'home.html', {'variable1':'Jitendra'})
	# return HttpResponse('This is home page.');

#about page function
def about(request):
	if not request.user.is_authenticated:
		return redirect('/login')

	return render(request, 'about.html')
	# return HttpResponse('This is about us page.')

#contact page function
def contact(request):
	if not request.user.is_authenticated:
		return redirect('/login')

	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		contact = Contact(fname = fname, lname= lname, email = email, phone = phone, message = message, date = datetime.today())
		contact.save()
		messages.success(request, 'Your message has been sent.')

	return render(request, 'contact.html')
	# return HttpResponse('This is contact us page.')


#balance_sheet page function
def balance_sheet(request):
	if not request.user.is_authenticated:
		return redirect('/login')

	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		messages.success(request, 'Your message has been sent.')

	return render(request, 'balance_sheet.html')
	# return HttpResponse('This is balance_sheet us page.')



# Crud Operation start
def crud_view(request):
	if not request.user.is_authenticated:
		return redirect('/login')

	""" cursor = connection.cursor()
	sql_query = "select * from employees limit 100"
	cursor.execute(sql_query)
	row_count = cursor.rowcount
	# result = cursor.fetchall()
	results = dictfetchall(cursor) """

	# fetch records form table
	results = Employees.objects.all()

	#search section
	emp_no = request.POST.get('emp_no')
	full_name = request.POST.get('full_name')
	filter_context = {
		'emp_no' : emp_no,
		'full_name' : full_name
	}

	if emp_no != '' and emp_no is not None:
		results = results.filter(emp_no = emp_no)

	if full_name != '' and full_name is not None:
		results = results.filter(first_name__icontains = full_name) | results.filter(last_name__icontains = full_name)	

	results = results[0:100]

	row_count =results.count()
	# pagination code
	page = request.GET.get('page', 1)
	paginator = Paginator(results, 10)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
		result = paginator.page(1)
	except EmptyPage:
		result = paginator.page(paginator.num_pages)
	
	return render(request, 'crud-view.html', {'datas' : result, 'row_count' : row_count, 'filter':filter_context})
	 
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
