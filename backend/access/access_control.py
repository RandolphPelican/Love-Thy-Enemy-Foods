from typing import Dict
from models.models import UserRole

class AccessControl:
    def __init__(self):
        self.admin_assigned = False
        self.user_roles: Dict[str, UserRole] = {}
    
    def initialize(self, caller: str):
        if caller != "anonymous":
            if caller not in self.user_roles:
                if not self.admin_assigned:
                    self.user_roles[caller] = UserRole.ADMIN
                    self.admin_assigned = True
                else:
                    self.user_roles[caller] = UserRole.USER
    
    def get_user_role(self, caller: str) -> UserRole:
        if caller == "anonymous":
            return UserRole.GUEST
        elif caller in self.user_roles:
            return self.user_roles[caller]
        else:
            raise Exception("User is not registered")
    
    def assign_role(self, caller: str, user: str, role: UserRole):
        if not self.is_admin(caller):
            raise Exception("Unauthorized: Only admins can assign user roles")
        self.user_roles[user] = role
    
    def has_permission(self, caller: str, required_role: UserRole) -> bool:
        role = self.get_user_role(caller)
        if role == UserRole.ADMIN:
            return True
        if required_role == UserRole.ADMIN:
            return False
        elif required_role == UserRole.USER:
            return role == UserRole.USER
        elif required_role == UserRole.GUEST:
            return True
        return False
    
    def is_admin(self, caller: str) -> bool:
        return self.get_user_role(caller) == UserRole.ADMIN
