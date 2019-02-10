import random


def test_delete_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) < 2:
        app.groups.add_new_group("my_new_group")
        old_list.append("my_new_group")
    group_del = random.choice(range(len(old_list)))
    app.groups.delete_group(group_del)
    new_list = app.groups.get_group_list()
    old_list.__delitem__(group_del)
    assert sorted(old_list) == sorted(new_list)
