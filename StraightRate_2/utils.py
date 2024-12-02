from django.contrib.auth.models import Group

PROPOSER_POINTS = 500
REDACTOR_POINTS = 5000


def update_user_groups(user):
    proposer_group, _ = Group.objects.get(name="Proposer")
    redactor_group, _ = Group.objects.get(name="Redactor")

    if user.points >= REDACTOR_POINTS:
        user.groups.add(redactor_group, proposer_group)
    elif user.points >= PROPOSER_POINTS:
        user.groups.add(proposer_group)
        user.groups.remove(redactor_group)
    else:
        user.groups.remove(proposer_group, redactor_group)

    user.save()
