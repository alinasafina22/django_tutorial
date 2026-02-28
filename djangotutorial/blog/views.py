from django.utils import timezone
from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:10]


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())
