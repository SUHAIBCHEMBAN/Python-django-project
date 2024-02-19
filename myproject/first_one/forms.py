# forms.py
from django import forms

def custom_email_validator(value):
    """
    validates that the email contains '@' and a domain with a dot.
    """
    if '@' not in value or '.' not in value.split('@')[-1]:
        raise forms.ValidationError("The email address must contain '@' and a valid domain.")

def custom_password_validator(value):
    """
    validates the password to have at least 8 characters, one digit, and one letter.
    """
    if len(value) < 8:
        raise forms.ValidationError("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in value):
        raise forms.ValidationError("Password must contain at least one digit")
    if not any(char.isalpha() for char in value):
        raise forms.ValidationError("Password must contain at least one letter")    

class SignUpForm(forms.Form):
    """
    form for user sign up.
    """
    username = forms.CharField(max_length=20)
    email = forms.EmailField(validators=[custom_email_validator])
    pass1 = forms.CharField(widget=forms.PasswordInput, validators=[custom_password_validator])
    pass2 = forms.CharField(widget=forms.PasswordInput, validators=[custom_password_validator])

    def clean(self):
        
        """ custom clean method to verify password confirmation """
        
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("pass1")
        pass2 = cleaned_data.get("pass2")

        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
