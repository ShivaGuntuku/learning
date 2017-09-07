from django import forms

class ContactForm(forms.Form):

	from_email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','placeholder': 'your email id'}),required=True)
	subject = forms.CharField(required=True,widget= forms.TextInput(attrs={'class':'form-control','placeholder':'your name'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'your message here'})) 