from django import forms

class ContactForm(forms.Form):

	from_email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'email-input','placeholder': 'your email id'}),required=True)
	subject = forms.CharField(required=True,widget= forms.TextInput(attrs={'class':'email-input','placeholder':'your name'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'text-area','placeholder':'your message here'})) 