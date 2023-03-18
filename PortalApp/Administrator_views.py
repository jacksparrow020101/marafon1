from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from PortalApp.models import Esasy_Surat, Habar, Metbugat, Metbugat_at, Surat, Wideo


class Bash_Sahypa(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Administrator/Baş Sahypa.html')


class Administrtor_Esasy_Surat(ListView):
    template_name = 'Administrator/Esasy Surat/Esasy_Surat_List.html'
    model = Esasy_Surat
    paginate_by = 100

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Esasy_Surat.objects.filter(
                Q(name__contains=filter_val, title__contains=filter_val)).order_by('-id')
        else:
            model = Esasy_Surat.objects.all()
        return model

    def get_context_data(self, **kwargs):
        context = super(Administrtor_Esasy_Surat, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Esasy surat'
        return context


class Administrator_Esasy_Surat_Create(SuccessMessageMixin, CreateView, ):
    template_name = 'Administrator/Esasy Surat/Esasy_Surat_Create.html'
    model = Esasy_Surat
    fields = '__all__'
    success_message = 'Maglumat goşuldy'

    def get_context_data(self, **kwargs):
        context = super(Administrator_Esasy_Surat_Create, self).get_context_data(**kwargs)
        context['title'] = 'Esasy suraty goşmak'
        return context


class Administrator_Esasy_Sahypa_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Esasy Surat/Esasy_Surat_Update.html'
    model = Esasy_Surat
    success_message = 'Maglumat üýtgedildi'
    fields = '__all__'


class Administrator_Esasy_Sahypa_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Esasy_Surat.objects.all(), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Esasy_Surat'))


class Administrator_Syyasy_Habar_List(ListView):
    template_name = 'Administrator/Habarlar/Syýasy Habar/Syýasy_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(name__contains=filter_val, habar_types=1)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=1).order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Syyasy_Habar_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Syýasy habarlar'
        context['name'] = 'Syýasy habarlar'
        return context


class Administrator_Syyasy_Habar_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Habarlar/Syýasy Habar/Syýasy_Habar_Create.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Syyasy_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Syyasy_Habar_Create, self).get_context_data()
        context['title'] = 'Syýasy habar goşmak'
        context['name'] = 'Syýasy habar goşmak'
        context['list'] = 'Syýasy habarlar'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.habar_types = '1'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Administrator_Syyasy_Habar_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Habarlar/Syýasy Habar/Syýasy_Habar_Update.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat üýtgedildi'
    success_url = reverse_lazy('Administrator_Syyasy_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Syyasy_Habar_Update, self).get_context_data()
        context['title'] = 'Syýasy habar üýtgetmek'
        context['name'] = 'Syýasy habar üýtgetmek'
        context['list'] = 'Syýasy habarlar'
        return context


class Administrator_Syyasy_Habar_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Habar.objects.filter(habar_types=1), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Syyasy_Habar_List'))


class Administrator_Tehnologiya_Habar_List(ListView):
    template_name = 'Administrator/Habarlar/Tehnologiýa Habar/Tehnologiya_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(name__contains=filter_val, habar_types=2)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=2).order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Tehnologiya_Habar_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Tehnologiýa habarlar'
        context['name'] = 'Tehnologiýa habarlar'
        return context


class Administrator_Tehnologiya_Habar_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Habarlar/Tehnologiýa Habar/Tehnologiya_Habar_Create.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Tehnologiya_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Tehnologiya_Habar_Create, self).get_context_data()
        context['title'] = 'Tehnologiýa habar goşmak'
        context['name'] = 'Tehnologiýa habar goşmak'
        context['list'] = 'Tehnologiýa habarlar'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.habar_types = '2'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Administrator_Tehnologiya_Habar_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Habarlar/Tehnologiýa Habar/Tehnologiya_Habar_Update.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat üýtgedildi'
    success_url = reverse_lazy('Administrator_Tehnologiya_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Tehnologiya_Habar_Update, self).get_context_data()
        context['title'] = 'Tehnologiýa habar üýtgetmek'
        context['name'] = 'Tehnologiýa habar üýtgetmek'
        context['list'] = 'Tehnologiýa habarlar'
        return context


class Administrator_Tehnologiya_Habar_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Habar.objects.filter(habar_types=2), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Tehnologiya_Habar_List'))


class Administrator_Sport_Habar_List(ListView):
    template_name = 'Administrator/Habarlar/Sport Habar/Sport_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(name__contains=filter_val, habar_types=3)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=3).order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Sport_Habar_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Sport habarlar'
        context['name'] = 'Sport habarlar'
        return context


class Administrator_Sport_Habar_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Habarlar/Sport Habar/Sport_Habar_Create.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Sport_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Sport_Habar_Create, self).get_context_data()
        context['title'] = 'Sport habar goşmak'
        context['name'] = 'Sport habar goşmak'
        context['list'] = 'Sport habarlar'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.habar_types = '3'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Administrator_Sport_Habar_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Habarlar/Sport Habar/Sport_Habar_Update.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat üýtgedildi'

    success_url = reverse_lazy('Administrator_Sport_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Sport_Habar_Update, self).get_context_data()
        context['title'] = 'Sport habar üýtgetmek'
        context['name'] = 'Sport habar üýtgetmek'
        context['list'] = 'Sport habarlar'
        return context


class Administrator_Sport_Habar_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Habar.objects.filter(habar_types=3), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Sport_Habar_List'))


class Administrator_Harby_Habar_List(ListView):
    template_name = 'Administrator/Habarlar/Harby Habar/Harby_Habarlar.html'
    model = Habar
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Habar.objects.filter(Q(name__contains=filter_val, habar_types=4)).order_by('-id')
        else:
            model = Habar.objects.filter(habar_types=4).order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Harby_Habar_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Harby habarlar'
        context['name'] = 'Harby habarlar'
        return context


class Administrator_Harby_Habar_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Habarlar/Harby Habar/Harby_Habar_Create.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Harby_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Harby_Habar_Create, self).get_context_data()
        context['title'] = 'Harby habar goşmak'
        context['name'] = 'Harby habar goşmak'
        context['list'] = 'Harby habarlar'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.habar_types = '4'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Administrator_Harby_Habar_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Habarlar/Harby Habar/Harby_Habar_Update.html'
    model = Habar
    fields = ['name', 'image', 'descriptions']
    success_message = 'Maglumat üýtgedildi'

    success_url = reverse_lazy('Administrator_Harby_Habar_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Harby_Habar_Update, self).get_context_data()
        context['title'] = 'Harby habar üýtgetmek'
        context['name'] = 'Harby habar üýtgetmek'
        context['list'] = 'Harby habarlar'
        return context


class Administrator_Harby_Habar_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Habar.objects.filter(habar_types=4), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Harby_Habar_List'))


class Administrator_Gazet_List(ListView):
    template_name = 'Administrator/Metbugat/Gazet/Gazet_List.html'
    model = Metbugat
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Metbugat.objects.filter(Q(ady__name__contains=filter_val, metbugat_type=1)).order_by('-id')
        else:
            model = Metbugat.objects.filter(metbugat_type=1).order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Gazet_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Gazetler'
        context['name'] = 'Gazetler'
        return context


class Administrator_Gazet_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Metbugat/Gazet/Gazet_Create.html'
    model = Metbugat
    fields = ['ady', 'image', 'pdf', 'date']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Gazet_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Gazet_Create, self).get_context_data()
        context['title'] = 'Harby habar goşmak'
        context['name'] = 'Harby habar goşmak'
        context['list'] = 'Harby habarlar'
        context['ady'] = Metbugat_at.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.metbugat_type = '1'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Administrator_Gazet_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Metbugat/Gazet/Gazet_Update.html'
    model = Metbugat
    success_message = 'Maglumat üýtgedildi'
    fields = ['ady', 'image', 'pdf', 'date']

    success_url = reverse_lazy('Administrator_Gazet_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Gazet_Update, self).get_context_data()
        context['title'] = 'Harby habar goşmak'
        context['name'] = 'Harby habar goşmak'
        context['list'] = 'Harby habarlar'
        context['ady'] = Metbugat_at.objects.all()
        return context


class Administrator_Gazet_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Metbugat.objects.filter(metbugat_type=1), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Gazet_List'))


class Administrator_Zurnal_List(ListView):
    template_name = 'Administrator/Metbugat/Zurnal/Zurnal_List.html'
    model = Metbugat
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Metbugat.objects.filter(Q(ady__name__contains=filter_val, metbugat_type=2)).order_by('-id')
        else:
            model = Metbugat.objects.filter(metbugat_type=2).order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Zurnal_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Žurnallar'
        context['name'] = 'Žurnallar'
        return context


class Administrator_Zurnal_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Metbugat/Zurnal/Zurnal_Create.html'
    model = Metbugat
    fields = ['ady', 'image', 'pdf', 'date']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Zurnal_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Zurnal_Create, self).get_context_data()
        context['title'] = 'Žurnaller goşmak'
        context['name'] = 'Žurnallar goşmak'
        context['list'] = 'Žurnallar'
        context['ady'] = Metbugat_at.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.metbugat_type = '2'
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class Administrator_Zurnal_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Metbugat/Zurnal/Zurnal_Update.html'
    model = Metbugat
    success_message = 'Maglumat üýtgedildi'
    fields = ['ady', 'image', 'pdf', 'date']

    success_url = reverse_lazy('Administrator_Zurnal_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Zurnal_Update, self).get_context_data()
        context['title'] = 'Žurnallar goşmak'
        context['name'] = 'Žurnallar goşmak'
        context['list'] = 'Žurnallar'
        context['ady'] = Metbugat_at.objects.all()
        return context


class Administrator_Zurnal_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Metbugat.objects.filter(metbugat_type=2), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Zurnal_List'))


class Administrator_Surat_List(SuccessMessageMixin, ListView):
    model = Surat
    template_name = 'Administrator/Surat/Surat_List.html'
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Surat.objects.filter(Q(name__contains=filter_val)).order_by('-id')
        else:
            model = Surat.objects.all().order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Surat_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Suratlar'
        context['name'] = 'Suratlar'
        return context


class Administrator_Surat_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Surat/Surat_Create.html'
    model = Surat
    fields = ['name', 'image']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Surat_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Surat_Create, self).get_context_data()
        context['title'] = 'Surat goşmak'
        context['name'] = 'Surat goşmak'
        context['list'] = 'Suratlar'
        return context


class Administrator_Surat_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Surat/Surat_Update.html'
    model = Surat
    success_message = 'Maglumat üýtgedildi'
    fields = ['name', 'image']

    success_url = reverse_lazy('Administrator_Surat_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Surat_Update, self).get_context_data()
        context['title'] = 'Surat goşmak'
        context['name'] = 'Surat goşmak'
        context['list'] = 'Suratlar'
        return context


class Administrator_Surat_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Surat.objects.all(), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Surat_List'))


class Administrator_Wideo_List(SuccessMessageMixin, ListView):
    model = Wideo
    template_name = 'Administrator/Wideo/Wideo_List.html'
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        order_by = self.request.GET.get('orderby', 'id')
        if filter_val != '':
            model = Wideo.objects.filter(Q(name__contains=filter_val)).order_by('-id')
        else:
            model = Wideo.objects.all().order_by('-id')
        return model

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Wideo_List, self).get_context_data()
        context['filter'] = self.request.GET.get('filter', '')
        context['orderby'] = self.request.GET.get('orderby', 'id')
        context['title'] = 'Wideolar'
        context['name'] = 'Wideolar'
        return context


class Administrator_Wideo_Create(SuccessMessageMixin, CreateView):
    template_name = 'Administrator/Wideo/Wideo_Create.html'
    model = Wideo
    fields = ['name', 'video']
    success_message = 'Maglumat goşuldy'

    success_url = reverse_lazy('Administrator_Wideo_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Wideo_Create, self).get_context_data()
        context['title'] = 'Wideo goşmak'
        context['name'] = 'Wideo goşmak'
        context['list'] = 'Wideolar'
        return context


class Administrator_Wideo_Update(SuccessMessageMixin, UpdateView):
    template_name = 'Administrator/Wideo/Wideo_Update.html'
    model = Wideo
    success_message = 'Maglumat üýtgedildi'
    fields = ['name', 'video']

    success_url = reverse_lazy('Administrator_Wideo_List')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Administrator_Wideo_Update, self).get_context_data()
        context['title'] = 'Wideo goşmak'
        context['name'] = 'Wideo goşmak'
        context['list'] = 'Wideolar'
        return context


class Administrator_Wideo_Delete(SuccessMessageMixin, View):
    success_message = 'Maglumat pozuldy'

    def get(self, request, **kwargs):
        try:
            model = get_object_or_404(Wideo.objects.all(), pk=kwargs['pk'])
            model.delete()
            messages.success(request, 'Maglumat Pozuldy')
        except:
            messages.error(request, 'Maglumat Pozulmady')
        return HttpResponseRedirect(reverse('Administrator_Wideo_List'))
