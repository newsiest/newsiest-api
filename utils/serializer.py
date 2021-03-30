import json

class DefaultSerializer:
    include = None
    exclude = ['_sa_instance_state', '_class']

    def __init__(self, obj):
        self.obj = obj

    def get_dict(self, include=None):
        if not include:
            include = self.include

        new_dict = {}
        for key, val in self.obj.__dict__.items():
            if self.include == None or key in self.include and str(key) not in self.exclude:
                serialized_attr = None
                try:
                    if hasattr(val, 'serializer'):
                        serialized_attr = val.serializer.get_dict()
                    else:
                        serialized_attr = self.get_dict(val)
                except:
                    try:
                        serialized_attr = json.dumps(val)
                    except:
                        serialized_attr = val.__dict__

                new_dict[key] = serialized_attr
        return new_dict


import app
from api.articles.models import NewsArticle, NewsSource
src = NewsSource(name='src')
art = NewsArticle(title='titr', source = src)
print(DefaultSerializer(art).get_dict())


class SerializerMixin:
    default_serializer = DefaultSerializer

    def to_dict(self):
        return self.serializer.get_dict()

    def __getstate__(self):
        pass

    def __setstate__(self, state):
        pass




