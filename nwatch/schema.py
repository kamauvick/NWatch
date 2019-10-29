import graphene

import watch.schema


class Query(watch.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
