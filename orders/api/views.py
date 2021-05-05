import stripe
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import authentication, permissions, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.views import APIView
