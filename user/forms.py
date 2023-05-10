from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=20, label="password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username            = forms.CharField(max_length=50, label="username")
    password            = forms.CharField(max_length=20, label="password", widget= forms.PasswordInput)
    confirm_password    = forms.CharField(max_length=20, label="confirm password", widget= forms.PasswordInput)
    
    
    def clean(self):
        """this function is a django built in function to check the validity of the inputs"""
        """ this function will check those input before the form is submitted"""
        
        clean_username          = self.cleaned_data.get("username")
        clean_password          = self.cleaned_data.get("password")
        clean_confirm_password  = self.cleaned_data.get("confirm_password")
        
        if clean_password and clean_confirm_password and clean_password != clean_confirm_password:
            """check if the password is correct and matches. if not raise error and return VALUES"""
            raise forms.ValidationError(" the entered passwords doesnt match! ") 
        else:
            VALUES = {
                "username": clean_username,
                "password": clean_password,
            }
            
        
        return VALUES