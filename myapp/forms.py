from django import forms

class createnewproject(forms.Form):
    name=forms.CharField(label='Nombre Proyecto',max_length='200')