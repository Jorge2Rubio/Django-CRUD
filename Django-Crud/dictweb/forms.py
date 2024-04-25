from django.forms import ModelForm
from .models import Students

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'