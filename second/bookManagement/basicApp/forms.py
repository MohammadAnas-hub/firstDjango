from django import forms
from .models import Repositories, Commit



class RepositoriesForm(forms.ModelForm):
    class Meta:
        model = Repositories
        fields = '__all__'

class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = '__all__'
