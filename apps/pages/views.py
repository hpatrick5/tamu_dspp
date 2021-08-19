import io
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView

from apps.file_upload.utils import aws_session


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"


class FileInformationView(TemplateView):
    template_name = "pages/file_info.html"


class WhyUseView(TemplateView):
    template_name = "pages/why_use.html"


class ResultsExplainedView(TemplateView):
    template_name = "pages/results_explained.html"


@login_required(login_url='/accounts/login/')
def download_data_from_bucket(request, path):
    bucket_name = os.getenv('BUCKET_NAME')

    session = aws_session()
    s3_resource = session.resource('s3')
    obj = s3_resource.Object(bucket_name, path)
    io_stream = io.BytesIO()
    obj.download_fileobj(io_stream)

    io_stream.seek(0)
    data = io_stream.read().decode('utf-8')

    response = HttpResponse(data, content_type="text/csv")
    response['Content-Disposition'] = "attachment;filename=" + path.split("/")[-1]
    return response


