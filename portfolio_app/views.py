from django.shortcuts import render, redirect
from portfolio_app.models import Experience, Project, About_Me, Contact, Education
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.core.mail import send_mail


def portfolio_app(request):
    all_edu = Education.objects.all
    all_exp = Experience.objects.all
    all_proj = Project.objects.all
    all_about = About_Me.objects.all
    context = {'all_exp': all_exp,
               'all_proj': all_proj, 'all_about': all_about, 'all_edu': all_edu}

    # Trying input here
    if request.method == 'POST':
        name = request.POST.get('message-email')
        email = request.POST.get('message-name')
        subject = request.POST.get('message-subject')
        message = request.POST.get('message-content')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        message = '''
        New Message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', [
                  'thomaslohanportfolio@gmail.com'])

        return render(request, 'portfolio_app.html', context)

    else:

        return render(request, 'portfolio_app.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404
