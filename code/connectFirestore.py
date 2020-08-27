from google.cloud import firestore
import random,string


def connect(collection_name):
    # Project ID is determined by the GCLOUD_PROJECT environment variable
    db = firestore.Client()
    # Add Documents
    collection_ref = db.collection(collection_name)

    return collection_ref

if __name__ == '__main__':
    collection_ref = connect('leMonde')

    ## Insert new text
    N=25
    doc_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    doc_attributes= {'title':'this is cute','date':'2020-08-26'}
    collection_ref.document(doc_id).set(doc_attributes)
