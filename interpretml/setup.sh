#!/usr/bin/env bash
shopt -s expand_aliases

HERE=$(dirname "$0")
VERSION=${1:-"stable"}
REPO=${2:-"https://github.com/interpretml/interpret"}
PKG=${3:-"interpret"}

#create local venv
. "$HERE/.setup/setup_env"
. "$AMLB_ROOT/frameworks/shared/setup.sh" "$HERE" true

if [[ "$VERSION" == "stable" ]]; then
  PIP install interpret
fi

PY -c 'import interpret; print("interpret version", interpret.__version__, "installed")'
