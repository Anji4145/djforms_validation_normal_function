from django import forms
from django.core import validators

def check_for_s(value):
    if value[0].lower() == 's':
        raise forms.ValidationError('name is satrting with s')
    
def length_for_value(value):
    if len(value) < 5:
        raise forms.ValidationError('lentght should be more than 5')

class StudentForm(forms.Form):
    sname =forms.CharField(max_length=20,validators=[check_for_s,validators.MinLengthValidator(5)])
    sage= forms.IntegerField()
    sid = forms.IntegerField()
    semail= forms.EmailField()
    remail = forms.EmailField()
    botcatch=forms.CharField(widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        e = self.cleaned_data['semail'] 
        r = self.cleaned_data['remail'] 
        if e != r:
            raise forms.ValidationErroralid('invalid email')

    def botcatcher(self):
        bot = self.changed_data['botcatch']
        if bot > 0:
            raise forms.ValidationError('bot error')
