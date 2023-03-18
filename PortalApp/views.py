from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import resolve, reverse
from django.views import View
from django.views.generic import ListView

from PortalApp.models import *


class Bash_Sahypa(View):
    def get(self, request, *args, **kwargs):
        esasy_surat_models = Esasy_Surat.objects.all()
        syyasy_habar_model = Habar.objects.filter(habar_types=1).order_by('-id').first()
        syyasy_habar_models = Habar.objects.filter(habar_types=1).order_by('-id')[1:4]
        tehnologiya_habarlar = Habar.objects.filter(habar_types=2).order_by('-id')[0:5]
        sport_habarlar = Habar.objects.filter(habar_types=3).order_by('-id')[:5]
        harby_habarlar = Habar.objects.filter(habar_types=4).order_by('-id')[:5]
        context = {
            'esasy_surat_models': esasy_surat_models,
            'syyasy_habar_model': syyasy_habar_model,
            'syyasy_habar_models': syyasy_habar_models,
            'tehnologiya_habarlar': tehnologiya_habarlar,
            'sport_habarlar': sport_habarlar,
            'harby_habarlar': harby_habarlar,
        }
        return render(request, 'Users/Baş Sahypa.html', context)


class Syyasy_Habar(View):
    def get(self, request, *args, **kwargs):
        habar_model = get_object_or_404(Habar.objects.filter(habar_types=1), pk=kwargs['pk'])
        habar_model.read += 1
        habar_model.save()
        habar_models = Habar.objects.filter(habar_types=1).order_by('-id')[1:4]
        context = {
            'habar_model': habar_model,
            'habar_models': habar_models,
            'title': 'Syýasy habar',
            'name': 'Syýasy Habarlar',
            'id': habar_model.id,
        }
        return render(request, 'Users/Syyasy_Habar.html', context)


class Syyasy_Habarlar(ListView):
    template_name = 'Users/Syyasy_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(habar_types=1, name__contains=filter_val)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=1)
        return model

    def get_context_data(self, **kwargs):
        context = super(Syyasy_Habarlar, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Syýasy Habarlar'
        context['name'] = 'Syýasy habarlar'
        context['url'] = resolve(self.request.path).url_name
        return context


class Tehnologiya_Habar(View):
    def get(self, request, *args, **kwargs):
        habar_model = get_object_or_404(Habar.objects.filter(habar_types=2), pk=kwargs['pk'])
        habar_model.read += 1
        habar_model.save()
        habar_models = Habar.objects.filter(habar_types=2).order_by('-id')[1:4]
        context = {
            'habar_model': habar_model,
            'habar_models': habar_models,
            'title': 'Tehnologiýa habar',
            'name': 'Tehnologiýa Habarlar',
            'id': habar_model.id,
        }
        return render(request, 'Users/Tehnologiya_Habar.html', context)


class Tehnologiya_Habarlar(ListView):
    template_name = 'Users/Tehnologiya_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(habar_types=2, name__contains=filter_val)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=2)
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Tehnologiya_Habarlar, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Tehnologiýa Habarlar'
        context['name'] = 'Tehnologiýa habarlar'
        context['url'] = resolve(self.request.path).url_name
        return context


class Sport_Habar(View):
    def get(self, request, *args, **kwargs):
        habar_model = get_object_or_404(Habar.objects.filter(habar_types=3), pk=kwargs['pk'])
        habar_model.read += 1
        habar_model.save()
        habar_models = Habar.objects.filter(habar_types=3).order_by('-id')[1:4]
        context = {
            'habar_model': habar_model,
            'habar_models': habar_models,
            'title': 'Sport habar',
            'name': 'Sport Habarlar',
            'id': habar_model.id,
        }
        return render(request, 'Users/Sport_Habar.html', context)


class Sport_Habarlar(ListView):
    template_name = 'Users/Sport_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(habar_types=3, name__contains=filter_val)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=3)
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Sport_Habarlar, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Sport Habarlar'
        context['name'] = 'Sport habarlar'
        context['url'] = resolve(self.request.path).url_name
        return context


class Harby_Habar(View):
    def get(self, request, *args, **kwargs):
        habar_model = get_object_or_404(Habar.objects.filter(habar_types=4), pk=kwargs['pk'])
        habar_model.read += 1
        habar_model.save()
        habar_models = Habar.objects.filter(habar_types=4).order_by('-id')[1:4]
        context = {
            'habar_model': habar_model,
            'habar_models': habar_models,
            'title': 'Harby habar',
            'name': 'Harby Habarlar',
            'id': habar_model.id,
        }
        return render(request, 'Users/Harby_Habar.html', context)


class Harby_Habarlar(ListView):
    template_name = 'Users/Harby_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(habar_types=4, name__contains=filter_val)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=4)
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Harby_Habarlar, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Harby Habarlar'
        context['name'] = 'Harby habarlar'
        context['url'] = resolve(self.request.path).url_name
        return context


class Gazetler(ListView):
    template_name = 'Users/Gazetlar.html'
    model = Metbugat
    paginate_by = 10

    def get_queryset(self):
        model = Metbugat.objects.filter(metbugat_type=1).order_by('-date').order_by('-id')
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Gazetler, self).get_context_data(**kwargs)
        context['title'] = 'Gazetler'
        models = []
        for model in Metbugat_at.objects.all():
            if Metbugat.objects.filter(metbugat_type=1, ady=model):
                model_list = {}
                model_list['name'] = model.name
                model_list['count'] = Metbugat.objects.filter(ady=model).count()
                models.append(model_list)
            else:
                continue
        context['gazetlar'] = models
        context['url'] = resolve(self.request.path).url_name
        return context


def Metbugat_count(request, *args, **kwargs):
    model = get_object_or_404(Metbugat.objects.all(), pk=kwargs['pk'])
    if kwargs['type'] == 'Read':
        model.read += 1
        model.save()
    elif kwargs['type'] == 'Download':
        model.download += 1
        model.save()
    return HttpResponseRedirect(kwargs['url'])


class Gazet(ListView):
    template_name = 'Users/Gazet.html'
    model = Metbugat
    paginate_by = 10

    def get_queryset(self):
        model = Metbugat.objects.filter(metbugat_type=1, ady__name=self.kwargs['name']).order_by('-date').order_by(
            '-id')
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Gazet, self).get_context_data(**kwargs)
        context['title'] = 'Gazetler'
        models = []
        for model in Metbugat_at.objects.all():
            if Metbugat.objects.filter(metbugat_type=1, ady=model):
                model_list = {}
                model_list['name'] = model.name
                model_list['count'] = Metbugat.objects.filter(ady=model).count()
                models.append(model_list)
            else:
                continue
        context['gazetlar'] = models
        context['url'] = 'Gazet'
        context['title'] = 'Gazet'
        context['name'] = self.kwargs['name']
        return context


class Zurnallar(ListView):
    template_name = 'Users/Zurnallar.html'
    model = Metbugat
    paginate_by = 9

    def get_queryset(self):
        model = Metbugat.objects.filter(metbugat_type=2).order_by('-date').order_by('-id')
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Zurnallar, self).get_context_data(**kwargs)
        context['title'] = 'Žurnallar'
        models = []
        for model in Metbugat_at.objects.all():
            if Metbugat.objects.filter(metbugat_type=2, ady=model):
                model_list = {}
                model_list['name'] = model.name
                model_list['count'] = Metbugat.objects.filter(ady=model).count()
                models.append(model_list)
            else:
                continue
        context['zurnallar'] = models
        context['url'] = resolve(self.request.path).url_name
        return context

class Zurnal(ListView):
    template_name = 'Users/Zurnal.html'
    model = Metbugat
    paginate_by = 10

    def get_queryset(self):
        model = Metbugat.objects.filter(metbugat_type=2, name__name=self.kwargs['name']).order_by('-date').order_by(
            '-id')
        return model

    def get_context_data(self, *args, **kwargs):
        context = super(Zurnal, self).get_context_data(**kwargs)
        context['title'] = 'Žurnal'
        models = []
        for model in Metbugat_at.objects.all():
            if Metbugat.objects.filter(metbugat_type=2, name=model):
                model_list = {}
                model_list['name'] = model.name
                model_list['count'] = Metbugat.objects.filter(name=model).count()
                models.append(model_list)
            else:
                continue
        context['zurnallar'] = models
        context['url'] = 'Gazet'
        context['name'] = self.kwargs['name']
        return context

class Wideo(ListView):
    template_name = 'Users/Wideo.html'
    model = Wideo
    paginate_by = 9



class Surat(ListView):
    template_name = 'Users/Suratlar.html'
    model = Surat
    paginate_by = 30