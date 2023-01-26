from mongoengine import StringField,IntField,DynamicDocument,Document , EmbeddedDocumentField,EmbeddedDocument,ListField,BooleanField

class CiTypeField(EmbeddedDocument):
    name = StringField(min_length=1, max_length=255)
    label = StringField(min_length=1, max_length=255)
    type = StringField(min_length=1, max_length=255, default="str")
    required = BooleanField(default=False)


class CiType(Document):
    meta = {"collection":"citypes"}
    # id = StringField(min_length=1,max_length=255)
    name = StringField(min_length=1,max_length=255,required=True,unique_with="version")
    label = StringField(min_length=1,max_length=255)
    version = IntField(min_value=1,max_value=10000,required=True,default=1)
    fields = ListField(EmbeddedDocumentField(CiTypeField))

    def __str__(self):
        return f"{self.id}:{self.name}/{self.label}"

class Ci(DynamicDocument):
    meta = {"collection":"cis"}