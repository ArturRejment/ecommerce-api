import random
import string

from .models import Discount


def generate_discount_code() -> Discount:
    letters = string.ascii_uppercase
    new_code = ''.join(random.choice(letters) for _ in range(20))
    try:
        discount = Discount.objects.get(code=new_code)
    except Discount.DoesNotExist:
        discount = Discount.objects.create(
            code=new_code,
            percentage_value=5,
            is_disposable=True,
            is_used=False,
        ).save()
        return discount
    else:
        return generate_discount_code()
