from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def news(request):
	return render(request, 'news.html', {})

def patients(request):
	return render(request, 'patients.html', {})

def services(request):
	return render(request, 'services.html', {})		

def appointment(request):
	if request.method == "POST":
		fname = request.POST["fname"]
		lname = request.POST["lname"]
		date = request.POST["date"]
		email = request.POST["email"]
		treatment = request.POST["treatment"]
		note = request.POST["note"]

		appointment = "First Name:" + fname + " Last Name " + lname + "Email: " + email + " Treatment: " + treatment +" Notes:" + notes +" Date:" + date 

		#send email
		send_mail(
			'Appointment Request', #subject
			appointment, #message
			email, #from email
			['daajill71@gmail.com', 'achiengdiana71@yahoo.com'], # to email
			)



		return render(request, 'appointment.html', {
			"fname": fname,
			"lname": lname,
			"date": date,
			"email": email,
			"date": date,
			"note": note,
			"treatment": treatment})

		

	else:
		return render(request, 'home.html', {})		



#def contact(request):
#	if request.method == "POST":
#		fullname = request.POST["fullname"]
#		return render(request, 'contact.html', {"fullname": fullname })	

#	else:
#		return render(request, 'contact.html', {})	
		
		
def contact(request):
	if request.method == "POST":

		#fname = request.POST.get("fname", False)
		fname = request.POST["fname"]
		#fullname = request.POST["fullname"]
		lname = request.POST["lname"]
		date = request.POST["date"]
		email = request.POST["email"]
		treatment = request.POST["treatment"]
		note = request.POST["note"]

		#send email
		send_mail(
			fname, #subject
			treatment, #message
			email, #from email
			['daajill71@gmail.com', 'achiengdiana71@yahoo.com'], # to email
			)



		return render(request, 'contact.html', {"fname": fname })	

	else:
		return render(request, 'contact.html', {})	

