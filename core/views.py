from django.views.generic.base import TemplateView
# from django.views.generic import CreateView, UpdateView

from django.db.models.query_utils import Q
from core.models import Author, Track

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

