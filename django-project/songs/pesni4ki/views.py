from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import Songs


class IndexView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'song_list'
    model = Songs
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Songs.objects.filter(song_title=query)
        else:
            return Songs.objects.all()


class SongDetailView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        try:
            song =  Songs.objects.get(pk=kwargs['pk'])
        except Songs.DoesNotExist:
            raise Http404('Тази песен не съществува')

        return render(request, 'song_detail.html', {'song': song})
