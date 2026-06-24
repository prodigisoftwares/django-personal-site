#!/usr/bin/env bash

clear
npm run tw:build
docker compose run --rm --entrypoint "" web python manage.py collectstatic --no-input
git status -u
