from io import BytesIO
import weasyprint
from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from django.core.files.base import File
from django.template.loader import get_template
from django.http import StreamingHttpResponse
from django.utils.translation import get_language, activate
from utils.utils.misc import md2h5

# Create your views here.
def get_cv_html(lang_code=None):
    if lang_code in settings.LANGUAGES_DICT.keys():
        activate(lang_code)
    path = settings.ABOUT_ME_CV_PATHS_DICT.get(get_language() or 'en')
    with open(path) as f:
        cv_md = f.read()
    cv_html = md2h5(cv_md,
                        context={
                            'gpg_url': static('abraham@odinfinch.xyz.pgp')
                        })
    return cv_html

def cv(request):
    return render(request, 'about_me/cv.html', {
        'cv_html': get_cv_html(),
        'settings': settings,
    })
def iter_cv_pdf(lang_code=None):
    cv_html = get_cv_html(lang_code)
    page_html_template = get_template(
        'about_me/cv_printed.html'
    )
    page_html = page_html_template.render({
        'cv_html': cv_html
    })
    output = BytesIO()
    weasyprint.HTML(string=page_html).write_pdf(target=output)
    output.seek(0)
    while True:
        content = output.read(File.DEFAULT_CHUNK_SIZE)
        if not content:
            break
        yield content
def cv_pdf(request):
    lang = request.GET.get('lang')
    resp =  StreamingHttpResponse(
        iter_cv_pdf(lang)
    )
    resp['Content-Disposition'] = 'attachment; filename=cv.pdf'
    resp['Content-Type'] = 'application/pdf'
    return resp
def about_me(request):
    path = settings.ABOUT_ME_MARKDOWN
    with open(path) as f:
        aboutme_md = f.read()
    aboutme_html = md2h5(aboutme_md)
    return render(request, 'about_me/aboutme.html', {'aboutme_html': aboutme_html})
