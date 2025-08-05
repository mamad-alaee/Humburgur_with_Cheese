from models.Role import Role
from models.User import User


def init_base_data():
    roles = list(Role.objects().as_pymongo())
    if len(roles) == 0:
        owner_role = Role(name="owner").save()
        admin_role = Role(name="admin").save()
        seller_role = Role(name="seller").save()
        customer_role = Role(name="customer").save()

        owner_user = {
            "full_name" : "Mohammad Alaee",
            "password" : "password",
            "email" : "email",
            "role" : owner_role
        }
        User(**owner_user).save()



        
