#coding=utf-8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Article

class LatestEntriesFeed(Feed):
    title = "MyBlog"
    link = "/rss"
    description = "MyBlog 站点文章更新。"
#数据
    def items(self):
        return Article.objects.order_by('-article_create_time')[:8]
#标题
    def item_title(self, item):
        return item.article_title
#简介
    def item_description(self, item):
        return item.article_synopsis

    # 生成连接
    def item_link(self, item):
        return reverse('blog', args=[item.pk])