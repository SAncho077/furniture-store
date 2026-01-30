from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import ContactRequest

import logging
logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_request = form.save(commit=False)
            contact_request.status = "new"
            contact_request.save()

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            question = form.cleaned_data['question'] or "Не указан"

            subject = f"Новая заявка с сайта от {name}"
            message = f'''
            Имя: {name}
            Телефон: {phone}
            Вопрос: {question}
            Дата: {contact_request.created_at}
            '''

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                    )
                logger.info(f"Заявка отправлена: {name}, {phone}")

            except Exception as e:
                logger.error(f"Ошибка отправки: {str(e)}")
                messages.error(request, 'Ошибка отправки email')
                return render(request, 'contact_app/home.html', {'form': form})

            messages.success(
                request,
                f"Спасибо, {name}! Ваша заявка №{contact_request.id} отправлена."
            )
            return redirect('contact')

        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')

    else:
        # ЕСЛИ ПОЛЬЗОВАТЕЛЬ ПРОСТО ЗАШЕЛ НА СТРАНИЦУ (GET запрос)
        form = ContactForm()  # Пустая форма

    # 9. Отображаем страницу с формой
    return render(request, 'contact_app/home.html', {'form': form, 'title': 'Про нас'})