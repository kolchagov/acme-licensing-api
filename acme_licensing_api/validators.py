from django.core.validators import RegexValidator

def app_version_validator():
    return RegexValidator(
        regex=r'^[0-9.]+(-(alpha|beta|rc|final)\d*)*$',
        message="App version required, must follow standard dot notation."
    )