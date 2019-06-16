
# intro
https://code.visualstudio.com/docs/languages/python


# guide
https://code.visualstudio.com/docs/python/python-tutorial

auto-completion
run current line, shift+entre

## edit

### auto completion

```
"python.autoComplete.extraPaths": [
    "C:/Program Files (x86)/Google/google_appengine",
    "C:/Program Files (x86)/Google/google_appengine/lib/flask-0.12"]
```

```
 "python.autoComplete.addBrackets": true,
 ```

### format
```
"python.formatting.autopep8Args": ["--max-line-length", "120", "--experimental"],
"python.formatting.yapfArgs": ["--style", "{based_on_style: chromium, indent_width: 20}"]
"python.formatting.blackArgs": ["--line-length", "100"]
```

### Refactoring



## debug

"stopOnEntry": true,
"pythonPath": "${workspaceFolder}/.venv"



# extension

## git graph

