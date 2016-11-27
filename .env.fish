source venv-kbsoftware_couk/bin/activate.fish
set -x DJANGO_SETTINGS_MODULE "settings.dev_patrick"
set -x OPBEAT_APP_ID "app-id"
set -x OPBEAT_ORGANIZATION_ID "organization-id"
set -x OPBEAT_SECRET_TOKEN "secret-token"
set -x RECAPTCHA_PRIVATE_KEY "your private key"
set -x RECAPTCHA_PUBLIC_KEY "your public key"
set -x SECRET_KEY "the_secret_key"
set -x STRIPE_PUBLISH_KEY "your_stripe_publish_key"
set -x STRIPE_SECRET_KEY "your_stripe_secret_key"
source .private
