from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    email = forms.EmailField()
    nombre = forms.CharField()


class LoginForm(forms.Form):
	user = forms.CharField()
	passwd = forms.CharField(widget=forms.PasswordInput)


class RegistroForm(forms.Form):
	user = forms.CharField()
	nombre = forms.CharField()
	apellido = forms.CharField()
	nacimiento = forms.DateField()
	#nacimiento = forms.DateField(initial=datetime.date.today)
	email = forms.EmailField()
	email_check = forms.EmailField()
	passwd = forms.CharField(widget=forms.PasswordInput)
	passwd_check = forms.CharField(widget=forms.PasswordInput)