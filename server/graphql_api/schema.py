
import graphene
from tasks.optimise_model import optimise

class Query(graphene.ObjectType):
    """The GraphQL root query.
    """
    optimise_model = graphene.ID(a = graphene.Int(), b = graphene.Int())

    def resolve_optimise_model(root, info, a, b):
        result = optimise.delay(a, b)
        return result.id

schema = graphene.Schema(query = Query)
