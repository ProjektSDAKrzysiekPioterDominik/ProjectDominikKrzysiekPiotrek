from django.forms import ModelForm, CharField
from Products.models import Products

class ProductForm(ModelForm):
    class Meta:
        model = Products

        fields = [
            "Id",
            "Date_added",
            "Is_listed",
            "Describe",
            "Image",
            "Price",
            "Product_name",
            "Id_category",
            "Id_client",
        ]

        title = CharField(min_length = 5, max_length = 256, required=True)

        # def clean(self):
        #     result = super().clean()
        #     logger.info(f"BookForm - clean run - result is {result}")
        #     return result
