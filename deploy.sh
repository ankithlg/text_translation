#!/bin/bash

echo "Deploying Translation App..."

# Example deployment to remote server
scp -r * youruser@yourserver:/var/www/text_translate

# Restart Flask app (via systemd or any service manager)
ssh youruser@yourserver 'sudo systemctl restart translation-app'

echo "Deployment completed."
