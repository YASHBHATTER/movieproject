from django import forms
from testapp.models import Movie
class Movieform(forms.ModelForm):
    class meta:
        model = Movie
        field ='__all__'