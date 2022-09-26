from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    # override ready method to register and use signals
    def ready(self): 
        import profiles.signals
        
