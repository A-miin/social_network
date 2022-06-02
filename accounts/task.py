from accounts.models import User
from celery import shared_task
from main.settings import CLEARBIT_BEARER_TOKEN


@shared_task
def fill_fields(pk):
    import requests
    user = User.objects.get(id=pk)
    url = f'https://person.clearbit.com/v1/people/email/{user.email}'
    headers = {"Authorization": f"Bearer {CLEARBIT_BEARER_TOKEN}"}
    data = requests.get(url, headers=headers).json()
    if 'name' in data.keys():
        if 'fullName' in data['name'].keys():
            user.fullName = data['name']['fullName']
    if 'location' in data.keys():
        user.location = data['location']
    if 'bio' in data.keys():
        user.bio = data['bio']
    if 'site' in data.keys():
        user.site = data['site']
    if 'avatar' in data.keys():
        user.avatar = data['avatar']
    user.save()
