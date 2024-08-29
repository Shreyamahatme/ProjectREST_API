from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'
    verbose_name = 'My Application'

    def ready(self):
        # You can put any startup code or import signals here if needed
        pass
