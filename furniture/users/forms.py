from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserProfileForm(UserChangeForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'profile-input'
        self.fields['image'].widget.attrs['class'] = 'custom-file-label'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username',
                  'email')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес эл. почты'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input-signup'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль'
        }
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'

    class Meta:
        model = User
        fields = ('username', 'password')