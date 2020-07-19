from django.shortcuts import render
from django.views.generic import TemplateView

class Dashboard(TemplateView):
    def __init__(self):
        self.template_name = "../templates/dashboard.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class User(TemplateView):
    def __init__(self):
        self.template_name = "../templates/user.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class Tables(TemplateView):
    def __init__(self):
        self.template_name = "../templates/tables.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class Typography(TemplateView):
    def __init__(self):
        self.template_name = "../templates/typography.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class Icons(TemplateView):
    def __init__(self):
        self.template_name = "../templates/icons.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class Maps(TemplateView):
    def __init__(self):
        self.template_name = "../templates/maps.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class Notifications(TemplateView):
    def __init__(self):
        self.template_name = "../templates/notifications.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

class Rtl(TemplateView):
    def __init__(self):
        self.template_name = "../templates/rtl.html"

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())



