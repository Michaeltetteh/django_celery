from django.shortcuts import render,reverse
from .forms import NewsletterForm
from django.http import HttpResponseRedirect
from .tasks import send_message


def newsletter_view(request):
    if request.method == "GET":
        form = NewsletterForm()
        return render(request,'newsletter/newsletter.html',{
            'form':form,
        })
    else:
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            send_message.delay(email)
            return HttpResponseRedirect(reverse('newsletter:newsletter-view'))
