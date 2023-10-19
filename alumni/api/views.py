from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Login' : '/api/login/',
        'Sign Up' : '/api/signup/',
        'Test Token' : '/api/test-token/',

        'Profile' : '/get-profile/',
        'Account Information' : '/get-account-info/',

        'Account Posts' : '/api/get-account-posts/<int:pk>/',
        'Feed Posts' : '/api/get-feed-posts/',
        'Create Post' : '/api/create-post/',
        'Get Post' : '/api/get-post/<int:pk>/',
        'Edit Post' : '/api/edit-post/<int:pk>/',
        'Like Post' : '/api/like-post/<int:pk>/',
        'Comment Post' : '/api/comment-post/<int:pk>/',
        'Get Comment' : '/api/get-comment/<int:pk>/',
        'Delete Post' : '/api/delete-post/<int:pk>/',
    }

    return Response(api_urls)


# Authentication
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key, "user":serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key, "user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testToken(request):
    return Response("passed for {}".format(request.user.email))


# Profile
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getSelfProfile(request):
    account = Account.objects.get(user=request.user)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getAccountInfo(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)

# Search
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def searchByName(request):
    accounts = Account.objects.filter(firstName__contains=request.data['name'], lastName__contains=request.data['name'])
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def searchByBranch(request):
    students = Student.objects.filter(branch__contains=request.data['branch'])
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def searchByBatch(request):
    students = Student.objects.filter(batch__contains=request.data['batch'])
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# Posts
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getAccountPosts(request, pk):
    account = Account.objects.get(id=pk)
    posts = Post.objects.filter(account=account)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getFeedPosts(request):
    posts = Post.objects.all().order_by('date_created')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def createPost(request):
    account = Account.objects.get(user=request.user)
    post = Account.objects.create(account=account)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getPost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def likePost(request, pk):
    account = Account.objects.get(user=request.user)
    post = Post.objects.get(id=pk)

    if post.likes.filter(account=account).exists():
        post.likes.filter(account=account).delete()
        return Response('Post unliked')
    else:
        post.likes.create(account=account)
        return Response('Post liked')   

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def commentPost(request, pk):
    account = Account.objects.get(user=request.user)
    post = Post.objects.get(id=pk)
    comment = Comment.objects.create(account=account, text=request.data['text'])
    post.comments.add(comment) 
    return Response('Comment posted')   

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def getComment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)   

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('Post successfully deleted!')