source venv-kbsoftware_couk/bin/activate.fish
set -x ALLOWED_HOSTS "abc,xyz"
set -x DJANGO_SETTINGS_MODULE "settings.dev_patrick"
set -x DOMAIN "www.kbsoftware.co.uk"
set -x OPBEAT_APP_ID "app-id"
set -x OPBEAT_ORGANIZATION_ID "organization-id"
set -x OPBEAT_SECRET_TOKEN "secret-token"
set -x SECRET_KEY "the_secret_key"
source .private
