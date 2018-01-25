import graphene
from graphene_django.types import DjangoObjectType

from . import models


class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (graphene.Node, )


class Query(graphene.AbstractType):
    all_messages = graphene.List(MessageType)

    @staticmethod
    def resolve_all_messages(args, context):
        return models.Message.objects.all()