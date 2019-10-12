from django.views.generic import TemplateView

from post.models import Post


class PostListView(TemplateView):
    template_name = 'post/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context.update({'posts': posts})

        return context
