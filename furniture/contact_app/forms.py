from django import forms
from django.core.validators import RegexValidator
from .models import ContactRequest
import re

class ContactForm(forms.ModelForm):
    phone_regex = RegexValidator(
        regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        message="Введите корректный номер телефона. Пример: +7 900 123 45 67")
    phone = forms.CharField(
        validators=[phone_regex],
        widget=forms.TextInput(attrs={
            'class': 'questions-form-input',
            'placeholder': '+7 900 555 77 88',
            'pattern': '^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
            'title': 'Формат: +7 900 123 45 67'
        })
    )

    class Meta:
        model = ContactRequest
        fields = ['name', 'phone', 'question', 'agree_to_processing']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'questions-form-input',
                'placeholder': 'Введите имя',
                'autocomplete': 'name'
            }),
            'question': forms.Textarea(attrs={
                'class': 'questions-form-textarea',
                'placeholder': 'Начните писать...',
            }),
        }

        labels = {
            'name': 'Ваше имя',
            'phone': 'Ваш телефон',
            'question': 'Какой у вас вопрос?',
            'agree_to_processing': 'Я даю свое согласие на обработку...',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')  #

        if phone:

            phone = re.sub(r'[^\d+]', '', phone)

            if phone.startswith('8'):
                phone = '+7' + phone[1:]

            if len(phone) < 11 or len(phone) > 12:
                raise forms.ValidationError("Номер телефона должен содержать 11 цифр")

            formatted = f"+7 ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:]}"
            return formatted

        return phone

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name.strip():
            raise forms.ValidationError("Имя не может быть пустым")

        if len(name) < 2:
            raise forms.ValidationError("Имя слишком короткое")

        if len(name) > 100:
            raise forms.ValidationError("Имя слишком длинное")

        return name.strip()