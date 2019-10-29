import graphene
from graphene_django import DjangoObjectType

from .models import Profile, Neighbourhood, Business, EmergencyContact, Post


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class NeighbourhoodType(DjangoObjectType):
    class Meta:
        model = Neighbourhood


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business


class EmergencyType(DjangoObjectType):
    class Meta:
        model = EmergencyContact


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    profiles = graphene.List(ProfileType)
    neighbourhoods = graphene.List(NeighbourhoodType)
    businesses = graphene.List(BusinessType)
    emergencies = graphene.List(EmergencyType)
    posts = graphene.List(PostType)

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_neighbourhoods(self, info, **kwargs):
        return Neighbourhood.objects.all()

    def resolve_businesses(self, info, **kwargs):
        return Business.objects.all()

    def resolve_emergencies(self, info, **kwargs):
        return EmergencyContact.objects.all()

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()


schema = graphene.Schema(query=Query, subscription=Query)
