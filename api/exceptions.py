from rest_framework.exceptions import ValidationError


class EmptyProducts(ValidationError):
    default_detail = 'At least one product should be specified'
