from models.models import UserProfile

class Migration:
    @staticmethod
    def run(old_data: dict) -> dict:
        user_profiles = {}
        if 'user_profiles' in old_data:
            for principal, old_profile in old_data['user_profiles'].items():
                user_profiles[principal] = UserProfile(
                    name=old_profile.get('name', ''),
                    email="",
                    phone=old_profile.get('contact_info', '')
                )
        return {
            'user_profiles': user_profiles,
            'products': {},
            'orders': {},
            'next_product_id': 0,
            'next_order_id': 0
        }
