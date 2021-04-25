from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput(
           attrs={
               'class': 'form-control',
               'placeholder': 'Write your TODO',
           } 
        ))