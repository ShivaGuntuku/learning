from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import render, redirect

from personalResume.forms import ContactForm
# Create your views here.

def home(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			custom_message = """Hi,I'm: {0} \n 
			and my Email is : {1},\n 
			I have message for you: {2} \n 
			This message came from you personal Site.
			Thanks And Regards,
			you're Assistant""".format(subject,from_email,message)
			
			try:
				send_mail(subject, custom_message, from_email, ['guntuku.shiva@gmail.com'])#message+'this custom mail from django site'+'from'+from_email
			except BadHeaderError:
				if True:
					# return HttpResponse('Invalid header found.')
					messages.error(request, 'your message not sent..try again..')
			if True:
				#return redirect('thanks')
				messages.success(request,"thank you..your respond sent to shiva.")
	return render(request, "index.html", {'form': form})
	#return render(request, "index.html")