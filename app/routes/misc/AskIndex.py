from app.routes.Classes import Ask


def indexer(user):

    asks = [i for i in Ask.objects(asker=user)]

    for i in enumerate(asks, 1):
        i[1].update(index=i[0])
        i[1].save()
