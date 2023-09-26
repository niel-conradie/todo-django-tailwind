from accounts.views.login import CustomLoginView
from accounts.views.logout import custom_logout_view
from accounts.views.profile_change import custom_profile_change_view
from accounts.views.profile import custom_profile_view
from accounts.views.signup import custom_signup_view


__all__ = [
    CustomLoginView,
    custom_logout_view,
    custom_profile_change_view,
    custom_profile_view,
    custom_signup_view,
]
