from django import forms


class CommentForm(forms.Form):
    nome1 = forms.CharField(max_length=20, label="Nome 1")
    nome2 = forms.CharField(max_length=20,label="Nome 2" )
    