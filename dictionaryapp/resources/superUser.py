from ..models import SuperUser


def get_super_user(email=None, password=None):
    try:
        super_user_object = SuperUser.objects.get(email=email, password=password)
        if super_user_object.password == password:
            return {'super_user_object': super_user_object,
                    'Message': "Successfully login"}
    except Exception as exception:
        print('------>', exception)
        return {'super_user_object': None,
                'message': "Admin does not exist please make sure you have added in database manually"}
