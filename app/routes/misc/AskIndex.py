from app.routes.Classes import Ask, User


def indexer(user):

    asks = [i for i in Ask.objects(asker=user)]

    for i in enumerate(asks, 1):
        i[1].index = i[0]
