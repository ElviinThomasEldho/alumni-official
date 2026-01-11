from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    # path('post-list/', views.postList, name="postList"),
    # path('post-detail/<str:pk>/', views.postDetail, name="postDetail"),
    # path('post-create/', views.postCreate, name="postCreate"),
    # path('post-update/<str:pk>/', views.postUpdate, name="postUpdate"),

    # Authentication
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('test-token/', views.testToken, name="testToken"),

    # Profile
    path('get-profile/', views.getSelfProfile, name="getSelfProfile"),
    path('get-account-info/<int:pk>/', views.getAccountInfo, name="getAccountInfo"),

    # Posts
    path('get-account-posts/<int:pk>/', views.getAccountPosts, name="getAccountPosts"),
    path('get-feed-posts/', views.getFeedPosts, name="getFeedPosts"),
    path('create-post/', views.createPost, name="createPost"),
    path('get-post/<int:pk>/', views.getPost, name="getPost"),
    path('edit-post/<int:pk>/', views.editPost, name="editPost"),
    path('like-post/<int:pk>/', views.likePost, name="likePost"),
    path('comment-post/<int:pk>/', views.commentPost, name="commentPost"),
    path('get-post-comments/<int:pk>/', views.getPostComments, name="getPostComments"),
    path('get-comment/<int:pk>/', views.getComment, name="getComment"),
    path('delete-post/<int:pk>/', views.deletePost, name="deletePost"),
    
    path('create-private-room/<int:pk>/', views.create_private_room, name="create_private_room"),
    path('create-group-room/', views.create_group_room, name="create_group_room"),
    path('get-room/<int:pk>/', views.get_room, name="get_room"),
]
