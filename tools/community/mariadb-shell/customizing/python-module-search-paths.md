---
description: >-
  How the Python interpreter bundled with MariaDB Shell finds modules, how to
  add your own directories to sys.path, and how to install third-party
  packages with mariadb-shell --pym pip.
---

# Python Module Search Paths

MariaDB Shell includes its own Python interpreter and standard library. Python mode, scripts run with `-f`, plugins, and startup scripts all use this interpreter, not a Python installation on your system. To import your own modules or third-party packages, they must be on the search path of the bundled interpreter, `sys.path`.

To see which Python version the shell bundles and where it looks for modules, run:

```sh
mariadb-shell --py -e "import sys; print(sys.version); print('\n'.join(sys.path))"
```

## The Default Search Path

`sys.path` contains these entries, in this order:

| Entry | Contents |
| --- | --- |
| Directories from `PYTHONPATH` | Only when the environment variable is set. |
| The bundled standard library | Directories under `lib/mariadb-shell/lib/` in the installation directory. |
| Your user site-packages directory | Packages installed with `pip install --user`. Python adds it only if the directory exists. |
| The bundled site-packages directory | Third-party packages that ship with the shell, and packages installed with `pip` without `--user`. |
| `lib/mariadb-shell/python-packages` | The shell's own `mysqlsh` package and its helpers. |

While the shell loads a [plugin](../extending-mariadb-shell/plugins.md), it also puts the plugin's parent directory first on `sys.path`, so that the plugin can import its own modules, and removes it again afterward.

MariaDB Shell has no environment variable of its own for the module search path. It honors the standard Python variables: `PYTHONPATH` adds directories, and on Linux and macOS, `PYTHONHOME` replaces the location of the standard library.

{% hint style="warning" %}
Because the shell reads the standard Python environment variables, a `PYTHONPATH` or `PYTHONHOME` that you set for another Python installation also affects MariaDB Shell. Packages built for a different Python version, or a `PYTHONHOME` that points to another installation, can make Python mode fail to start. Unset these variables for the shell, or add directories in the startup script instead.
{% endhint %}

## Adding Directories

To make the modules in a directory importable in every session, add the directory in your [startup script](startup-scripts.md):

{% code title="~/.mariadb-shell/mariadb-shellrc.py" %}
```python
import os
import sys

sys.path.append(os.path.expanduser("~/dba-scripts"))
```
{% endcode %}

The startup script runs only when Python mode is initialized. Plugins and the files in `init.d` load at startup, possibly before the startup script runs, so they should not rely on directories that the startup script adds. A plugin can extend `sys.path` itself, or import its helper modules through its own package name.

For a single run, set `PYTHONPATH` on the command line:

```sh
PYTHONPATH=~/dba-scripts mariadb-shell --py -f nightly_check.py
```

## Installing Packages

To install a third-party package for the bundled interpreter, run `pip` through the shell with `--pym`, which runs a Python module as a script, like `python -m`. A `pip` from your system Python installs into that Python, where the shell doesn't find the package.

Install into your user site-packages directory with `--user`. This doesn't need write access to the installation directory, and the packages survive an upgrade or reinstallation of the shell:

```sh
mariadb-shell --pym pip install --user tabulate
```

Then use the package in Python mode:

```text
MariaDB localhost:3306 ssl  Py > from tabulate import tabulate
MariaDB localhost:3306 ssl  Py > rows = session.run_sql("SELECT name, population FROM world.country ORDER BY population DESC LIMIT 3").fetch_all()
MariaDB localhost:3306 ssl  Py > print(tabulate([[r[0], r[1]] for r in rows], headers=["Country", "Population"]))
Country          Population
-------------  ------------
China            1277558000
India            1013662000
United States     278357000
```

To find out where `--user` installs packages, run:

```sh
mariadb-shell --py -e "import site; print(site.getusersitepackages())"
```

Other useful `pip` commands:

```sh
mariadb-shell --pym pip list                   # installed packages
mariadb-shell --pym pip show tabulate          # details of one package
mariadb-shell --pym pip uninstall tabulate
mariadb-shell --pym pip install --target ~/shell-libs tabulate   # into a directory you add to sys.path
```

Without `--user` or `--target`, `pip` installs into the bundled site-packages directory inside the installation. That requires write access to the installation directory, and the packages are lost when you upgrade or reinstall MariaDB Shell.

{% hint style="info" %}
Packages with compiled extensions must match the bundled Python version and your platform. `pip` selects matching wheels automatically when they're available for the bundled version.
{% endhint %}
