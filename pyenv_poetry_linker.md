
### Add to Shell Config with Dynamic Detection
If you prefer a shell-based solution, add this to your .bashrc or .zshrc:
```bash
export LD_LIBRARY_PATH="$(pyenv prefix)/lib:$LD_LIBRARY_PATH"
```
This dynamically sets the path based on the current Pyenv version.