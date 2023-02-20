from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')


    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()



    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_page_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_page_url = ''

    if page.has_next():
        next_page_url = '?page={}'.format(page.next_page_number())
    else:
        next_page_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_page_url': next_page_url,
        'prev_page_url': prev_page_url,
    }


    return render(request, 'blog/index.html', context=context)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetails(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'


class TagDetails(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_details.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True



class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    form_model = TagForm
    template = 'blog/tag_update.html'
    model = Tag
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    form_model = PostForm
    template = 'blog/post_update.html'
    model = Post
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'
    raise_exception = True








