class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True
    elif group.get_groups() == [] :
        return False
    else:
        subgroups = group.get_groups()
        for subgroup in subgroups:
            if is_user_in_group(user,subgroup ) == True:
                return True
        return False

        
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")
sub_child_user = "sub_child_user"
sub_child2.add_user(sub_child_user)
child.add_group(sub_child)
child.add_group(sub_child2)
parent.add_group(child)

def test(user, group, expected_output):
    if is_user_in_group(user, group) == expected_output:
        if expected_output == False:
            print('Pass: {} not in {} group'.format(user, group.get_name()))
        else:
            print('Pass: {} in {} group'.format(user, group.get_name()))
    else:
        print('Fail')

test(sub_child_user, parent, True)
test(sub_child_user, sub_child2, True)
test('Not a user', parent, False)
test('', parent, False)
test(None, parent, False)
test(sub_child_user, sub_child, False)