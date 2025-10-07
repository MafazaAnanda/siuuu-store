from django.utils.html import strip_tags
from django.forms import ModelForm
from main.models import Item

class Itemsform(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "stock", "brand"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)