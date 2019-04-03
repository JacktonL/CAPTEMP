from app.routes.Classes import Ask, User


def indexer(user):

    asks = [i for i in Ask.objects(asker=user)]
