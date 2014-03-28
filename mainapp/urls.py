from django.conf.urls import patterns, url

from mainapp import views

urlpatterns = patterns('',
    #Actions
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^post_new/', views.post_new, name='post_new'),
    url(r'^signup_do/', views.signup_do, name='signup_do'),
    url(r'^login_do/', views.login_do, name='login_do'),
    url(r'^cancel_post/', views.cancel_post, name='cancel_post'),
    url(r'^logout_do/', views.logout_do, name='logout_do'),
    url(r'^reserve/', views.reserve, name='reserve'),
    url(r'^accept/', views.accept, name='accept'),
    url(r'^cancel_res/', views.cancel_res, name='cancel_res'),
    url(r'^revoke/', views.revoke, name='revoke'),
    url(r'^search_do/', views.search_do, name='search_do'),
    url(r'^edit_post/', views.edit_post, name='edit_post'),
    url(r'^send_message/', views.send_message, name='send_message'),
    url(r'^view_messages/', views.view_messages, name='view_messages'),
    url(r'^delete_message/', views.delete_message, name='delete_message'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^send_verification_email/', views.send_verification_email, name='send_verification_email'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    
    
    #Pages
    url(r'^signup_page/', views.signup_page, name='signup_page'),
    url(r'^post_form/', views.post_form, name='post_form'),
    url(r'^post_page/', views.post_page, name='post_page'),
    url(r'^login_page/', views.login_page, name='login_page'),
    url(r'^index/', views.index, name='index'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^reserve_page/', views.reserve_page, name='reserve_page'),
    url(r'^edit_profile_page/', views.edit_profile_page, name='edit_profile_page'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^inbox/', views.inbox_page, name='inbox_page'),
)