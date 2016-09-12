
from django.conf.urls import patterns, include, url 

import views

urlpatterns = patterns('',
    url(r'^(\w+)/articles-list/(\d+)/$', views.articles_list, name='articles_list'),
    url(r'^(\w+)/article-detail/(\d+)/$', views.article_detail, name='article_detail'),
    url(r'^(\w+)/open-account/$', views.open_account, name='open_account'),
    url(r'^(\w+)/sim-account/$', views.sim_account, name='sim_account'),
    url(r'^(\w+)/activity-user/(\d+)/$', views.activity_user, name='activity_user'),
    url(r'^(\w+)/commit-success/$', views.commit_success, name='commit_success'),
    url(r'^(\w+)/commit-fail/$', views.commit_fail, name='commit_fail'),
    url(r'^(\w+)/activity-list/$', views.activity_list, name='activity_list'),
    url(r'^(\w+)/show_question/$', views.show_question, name='show_question'),
    url(r'^(\w+)/activity-add/$', views.activity_add, name='activity_add'),
    url(r'^(\w+)/proposal-add/$', views.proposal_add, name='proposal_add'),
    url(r'^(\w+)/proposal-list/$', views.proposal_list, name='proposal_list'),
    url(r'^(\w+)/proposal_seconded/(\d+)/$', views.proposal_seconded, name='proposal_seconded'),
    url(r'^(\w+)/proposal_discuss/(\d+)/$', views.proposal_discuss, name='proposal_discuss'),
    url(r'^(\w+)/proposal_vote/(\d+)/$', views.proposal_vote, name='proposal_vote'),
)
