from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Blog, Tag, About


class BlogListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    model = Blog
    paginate_by = 3
    queryset = Blog.objects.filter(publish=True).order_by('-date')


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['similar_blog'] = Blog.objects.all().order_by('?')[:3]
        self.object.visit_count += 1
        self.object.save()
        context['next_blog'] = Blog.objects.filter(id__gt=self.object.id).order_by('id')[:1]
        context['previous_blog'] = Blog.objects.filter(id__lt=self.object.id).order_by('-id')[:1]
        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = About.get_solo()
        return context

# class TagView(ListView):
#     template_name = 'blog/taggedblog.html'
#     context_object_name = 'blogentry'
#
#     def get_queryset(self):
#         return Post.objects.filter(tags__slug=self.kwargs['slug'])
#
#     def get_context_data(self, **kwargs):
#         context = super(TagView, self).get_context_data(**kwargs)
#         context['hot_blogs'] = Post.objects.filter(is_hot=True)[:8]
#         context['featured_blogs'] = Post.objects.filter(is_featured=True)[:3]
#         context['popular_blogs'] = Post.objects.all().order_by('-visit_count')[:3]
#         context['popular_tags'] = Tag.objects.all().order_by('-visit_count')[:5]
#         context['tags'] = Tag.objects.all()
#         context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
#         return context