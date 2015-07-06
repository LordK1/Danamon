from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from Danamon import settings
from newsletter.forms import SignUpForm, ContactForm
from newsletter.models import SignUp


def home(request):
    form = SignUpForm(request.POST or None)

    context = {
        'title': "Sign Up",
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = "new full name"
        instance.full_name = full_name

        if not instance.full_name:
            instance.full_name = "Keyvan"

        instance.save()
        context = {
            'title': "thank you %s" % instance.full_name
        }

    if request.user.is_authenticated() and request.user.is_staff:
        # print(SignUp.objects.all())
        for instance in SignUp.objects.all():
            print(instance.full_name)

        queryset = SignUp.objects.all().order_by('-timestamp')#.filter(full_name__iexact='keyvan')
        context = {
            "queryset": queryset
        }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact Us',
        'form': form,
        'title_align_center': True
    }

    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print(key, value)

        form_full_name = form.cleaned_data.get('full_name')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')

        subject = 'Site Contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'youremail@email.com']

        contact_message = "%s: %s via %s" % (
            form_full_name, form_message, form_email)

        html_message = "<h1>Hello this message sent from Django Mail via LORDK1 :)) </h1>"
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            html_message=html_message,
            fail_silently=False
        )
        # print(email, full_name, message)

    return render(request, "newsletter/forms.html", context)


def search(request):
    if request.POST:
        print request.POST['term']
        return HttpResponseRedirect("/")
    else:
        return render_to_response('newsletter/search.html')
