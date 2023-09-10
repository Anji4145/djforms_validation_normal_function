from django import forms

def check_for_s(value):
    if value[0].lower() == 's':
        raise forms.ValidationError('name is satrting with s')
    
def length_for_value(value):
    if len(value) < 5:
        raise forms.ValidationError('lentght should be more than 5')

class StudentForm(forms.Form):
    sname =forms.CharField(max_length=20,validators=[check_for_s,length_for_value])
    sage= forms.IntegerField()
    sid = forms.IntegerField()
    semail= forms.EmailField(validators=[check_for_s]) 