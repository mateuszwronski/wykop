from django.views.generic import TemplateView

from post.models import Post


class PostListView(TemplateView):
    template_name = 'post/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context.update({'posts': posts})

        return context


class PostDetailView(TemplateView):
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = kwargs.get('pk')
        post = Post.objects.get(id=pk)
        context.update({'post': post})

        return context
