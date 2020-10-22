# from django.views.generic import CreateView, UpdateView
from django.db.models.query_utils import Q
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
from django.views.generic.base import TemplateView
from django.db.models.aggregates import Count, Sum, Avg

from core.models import Author, Track
from core.forms import TrackCreateForm

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        tracks = Track.objects.all()

        context = {
            'greet': "Hello world!",
            'tracks': tracks
        }

        if 'query' in self.request.GET:
            context['query'] = self.request.GET['query']
            # tracks = tracks.filter(**{'name': 'asdasd'}
            tracks = tracks.filter(
                Q(name__icontains=self.request.GET['query']) |
                Q(author__name__icontains=self.request.GET['query']) |
                Q(genre__name__icontains=self.request.GET['query'])
                # duration="3:33"
            )
            # tracks.filter(**{'name':  'qwe'})
            context['tracks'] = tracks


        # print(self.request.GET['query'])
        # tracks = Track.objects.all().select_related(
        #     'author',
        #     'genre'
        # ).order_by('-genre__name')

        # tracks = Track.objects.filter(name="Некромант")
        return context

    # def get(self, request, *args, **kwargs):
    #     pass

    # def post(self, request):
    #     pass


class NewIndex(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        tracks = Track.objects.all().select_related().prefetch_related('tags').values('id', 'name', 'duration')
        # artists = Author.objects.all().prefetch_related('tracks')
        print(tracks)
        artists = Author.objects.all().annotate(
            track_count=Count('tracks'),
            all_duration=Avg('tracks__duration')
        ).filter(track_count__gt=0)

        context = {
            'greet': "Hello world!",
            'tracks': tracks,
            'artists': artists
        }
        return context

# class TrackCreateView(TemplateView):
#     template_name = 'create_track.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(TrackCreateView, self).get_context_data(**kwargs)
#         context['form'] = TrackCreateForm()
#         return context
#
#     def post(self, request):
#         form = TrackCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#         return self.render_to_response({'form': form})

# class TrackCreateView(FormView):
#     template_name = 'create_track.html'
#     form_class = TrackCreateForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.save()
#         return super(TrackCreateView, self).form_valid(form)

    # def form_invalid(self, form):
    #     pass

class TrackCreateView(CreateView):
    template_name = 'create_track.html'
    success_url = '/'
    model = Track
    fields = '__all__'
    # Виджеты тут создавать нельзя, прийдется модел форму создавать см. выше


# class CreateAuthorView(CreateView):
#     template_name = "create_author.html"
#     model = Author
#     fields = '__all__'
#     success_url = '/'

# class UpdateAuthorView(UpdateView):
#     template_name = "create_author.html"
#     model = Author
#     fields = '__all__'
#     success_url = '/'

