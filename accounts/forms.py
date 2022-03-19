from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=125, required=True)
    password = forms.CharField(max_length=125, required=True)
    
    class Meta:
        fields = '__all__'
    
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control border-input'}),
            'password': forms.PasswordInput(attrs={'class':'form-control border-input'}),
        }
