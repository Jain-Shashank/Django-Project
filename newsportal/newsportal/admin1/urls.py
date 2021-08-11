 # Url file of admin1
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.master1),
	path('user_profile', views.user_profile),
	# path('approverRights', views.Approver_rights),
	path('contentCategory', views.Content_category),
	path('mediaRepoterInformation', views.media_repoter_information),
	# path('newsPortalLogin', views.News_portal_login),
	path('newsUpdate', views.News_update),
	path('userDetail', views.User_detail),
	path('login', views.login),
	path('register', views.register),
	path('logout', views.logout),
	path('delete_data/<int:id>', views.delete_data),
	path('delete_media_data/<int:id>', views.delete_media_data),
	path('delete_user_data/<int:id>', views.delete_user_data),
	path('block_user/<int:id>', views.block_user),
	path('edit_data/<int:id>', views.edit_data),
	path('edit_data_stored/<int:id>', views.edit_data_stored),
	path('show_news_content_data/<int:id>', views.show_content_data),
	path('delete_content_data/<int:id>', views.delete_content_data),
	path('block_user/<int:id>', views.block_user),	
	path('news_update/<int:id>', views.news_update),
	path('show_data', views.show_data),		
	path('edit_profile', views.edit_profile), 
	path('total_News', views.total_News),
    path('Approved_News', views.Approved_News),
    path('pending', views.pending),
    path('data_comments', views.data_comments),
    path('show_block', views.show_block),
    path('unshow_block', views.unshow_block),
    path('show_reporter', views.show_reporter),    
    path('categorie', views.categorie),  
    path('admin_feedback', views.admin_feedback),
    path('del_admin_feedback/<int:id>', views.del_admin_feedback),    
]