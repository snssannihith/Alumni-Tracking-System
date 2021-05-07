from django import forms
from .models import AdminModel, StudentModel

DEPARTMENT_CHOICES = (
    ('IT', 'IT'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('MECH', 'MECH'),
    ('CIVIL', 'CIVIL')
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)


class AdminSearchForm(forms.Form):
    department = forms.ModelChoiceField(queryset=AdminModel.objects.values_list('department', flat=True).distinct(),
                                        to_field_name='department')


class AdminForm(forms.Form):
    department = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    phone = forms.CharField(max_length=10)

    def clean_department(self):
        dept = self.cleaned_data['department']
        if AdminModel.objects.filter(department__icontains=dept).exists():
            raise forms.ValidationError("Department already allocated")
        return dept


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    hall_ticket_no = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)
    phone = forms.CharField(max_length=10)
    year_of_passing = forms.IntegerField()

    def clean_hall_ticket_no(self):
        print('pramod')
        no = self.cleaned_data['hall_ticket_no']
        if StudentModel.objects.filter(hall_ticket_no=no.upper()).exists():
            print('pramod2')
            raise forms.ValidationError("Already exists")
        return no
