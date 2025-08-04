# HOWTOS

## How to Dinamically Link PYENV and POETRY

### Add to Shell Config with Dynamic Detection
Add this to your .bashrc or .zshrc:

```bash
#------------- Pyenv + Poetry -----------
export LD_LIBRARY_PATH="$(pyenv prefix)/lib:$LD_LIBRARY_PATH"
# ---------------------------------------
```

This dynamically sets the path based on the current Pyenv version.

## How to Export Poetry to Requirements
use helper script [poetry_export.sh](poetry_export.sh)
```bash
poetry_export.sh
```

## How to Create, Up or Remove Docker
There is [Makefile](Makefile) giving shortcut to manage docker
```bash
make dev-down
make dev-image
make dev-up
make dev-migrate
make dev-collecstatic
make staging-up
make prod-image
```

