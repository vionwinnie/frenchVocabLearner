# from django.db import models
# Create your models here.
from fireo.models import Model,NestedModel
from fireo.fields import TextField,NumberField,ListField
import fireo

class Vocabulary(Model):
    vocab = ListField()

class Lemonde(Model):
    date = TextField()
    num_paragraphs = NumberField()
    paragraphs = ListField()
    title = TextField()
    vocab = NestedModel(Vocabulary)


if __name__ == '__main__':
    articles= Lemonde.collection.fetch()
    for article in articles:
        print(article.id, article.num_paragraphs)
        if article.paragraphs:
            print(article.paragraphs[0])

