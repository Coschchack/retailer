from django.urls import reverse


class ApiUrls:
    def get_product_list_url(*args):
        return reverse("product-list", args=args)

    def get_product_detail_url(*args):
        return reverse("product-detail", args=args)

    def get_order_list_url(*args):
        return reverse("order-list", args=args)

    def get_order_detail_url(*args):
        return reverse("order-detail", args=args)
