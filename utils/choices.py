def status_choice():
    STATUS_CHOICE = (
        (1, 'active'),
        (0, 'inactive'),
    )
    return STATUS_CHOICE


def sale_choices():
    SALE_CHOICES = (
        (0, 'no'),
        (1, 'yes')
    )

    return SALE_CHOICES


def cart_choices():
    CART_CHOICES = (
        (0, 'cart'),
        (1, 'buy')
    )
    return CART_CHOICES
