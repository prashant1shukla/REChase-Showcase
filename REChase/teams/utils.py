import random

from .models import (
    Team,
)


def makeCode():
    used = set(Team.objects.all().values_list('code', flat=True))
    code = str(random.randint(100000, 999999))
    while code in used:
        code = str(random.randint(100000, 999999))
    return code
