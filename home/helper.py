from django.utils.text import slugify

import secrets
import string


def generate_random_string(N):
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for i in range(N))
    return res


def generate_slug(text):
    from home.models import BlogModel
    new_slug = slugify(text)
    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(6))
    return new_slug
