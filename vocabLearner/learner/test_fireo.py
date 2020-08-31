from fireo.models import Model
from fireo.fields import TextField,NumberField,ListField
import fireo

## This is a collection
class User(Model):
    ## this is the field 
    name = TextField()

class LeMonde(Model):
    date = TextField()
    num_paragraphs = NumberField()
    paragraphs = ListField()
    title = TextField()

class Pokemon(Model):
    name = TextField()
    weight = NumberField()
    paragraphs = ListField()


#u = User()
#u.name = "Azeem Haider"
#u.save()

# Get user
#user = User.collection.get(u.key)
#print(u.key)
#print(type(u.key))
#print(user.name)

## all collections:
pokemons = Pokemon.collection.fetch()
for poke in pokemons:
    print(poke.id,poke.name,poke.weight)
    cur_para = poke.paragraphs
    if cur_para:
        for para in cur_para:
            print(para)

#articles= LeMonde.collection.fetch()
#for article in articles:
#    print(article)
#    print(article.id, article.num_paragraphs)

