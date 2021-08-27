import graphene
from graphene import ObjectType, String

class ExampleQuery(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return 'Hello'

shema = graphene.Schema(query=ExampleQuery)  
