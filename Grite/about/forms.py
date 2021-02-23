from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', required=True)
    from_email = forms.EmailField(label='E-mail', required=True)
    phone = forms.CharField(label='Телефон', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


