from django import forms
from users.models import College, WorkExp

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=10)
    email = forms.CharField(max_length=50)


class CollegeForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = College
        fields = ('college_name', 'specialization', 'year_of_passing', 'address')


class WorkForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = WorkExp
        fields = ('company', 'role', 'start_year', 'end_year', 'address')


class SearchForm(forms.Form):
    hall_ticket_no = forms.CharField(max_length=10, required=False)
    year_of_passing = forms.IntegerField(required=False)
    department = forms.CharField(max_length=10, required=False)
    college_name = forms.CharField(max_length=50, label='College', required=False)
    clg_address = forms.CharField(max_length=50, label="Address", required=False)
    clg_yop = forms.IntegerField(label='Year of Passing', required=False)
    company = forms.CharField(max_length=20, required=False)
    role = forms.CharField(max_length=20, required=False)
    cmp_add = forms.CharField(max_length=50, label="Address", required=False)

