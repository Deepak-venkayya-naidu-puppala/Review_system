from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,widget=
    forms.TextInput(attrs={'class' : 'form-name','placeholder':'Name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-message','placeholder':'Review'}))
