
# Nom du projet

## Groupe projet
- Étud. 1 : POINGT, Thomas (22302515)
- Étud. 2 : BARY, Joséphine (22201052)
- Étud. 3 : CHAPOUTOT, Kélian (22300928)
- Étud. 4 : COUETTE, Xavier (22301601)
- Groupe TD : S2MITD04

## Prérequis
* Un interpréteur Python (version >= 3.11)
  * en février 2024 :
    3.11 ([Debian](https://packages.debian.org/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)),
    3.8 ([Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/20.04),
    3.10 ([Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/22.04),
    3.11 ([Ubuntu](https://packages.ubuntu.com/search?keywords=python3&searchon=names&exact=1&suite=all&section=all)/23.04),
    3.12 ([Windows/python.org](https://www.python.org/downloads/windows/)), 3.12 ([Mac OS X/python.org](https://www.python.org/downloads/mac-osx/)),
    3.11 ([Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)/tous systèmes),
    3.12 ([python.org](https://www.python.org/downloads/)/tous systèmes)
* Le gestionnaire de paquets Python [`pip`](https://pip.pypa.io/en/stable/)
  * la distribution Python de [python.org](https://www.python.org/) à partir de la version 3.4 contient `pip`
* Le module `venv` pour la gestion des environnements virtuels ([tutoriel](https://docs.python.org/3/tutorial/venv.html))
  * Le module `venv` existe dans la bibliothèque standard Python depuis la version 3.3
* Un IDE
  * par exemple, [Visual Studio Code](https://code.visualstudio.com/) avec l'extension [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) ([tutoriel](https://code.visualstudio.com/docs/python/python-tutorial))

### Remarques
* Les distributions Python de [python.org](https://www.python.org/) ou [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html) fournissent de base l'ensemble des prérequis Python.
* L'installation de base de la distribution Anaconda contient l'IDE [Spyder](https://www.spyder-ide.org/) et les notebooks [Jupyter](https://jupyter.org/). Ce n'est pas le cas de Miniconda qui est beaucoup plus légère (400 Mo contre 3 Go).
* L'installation de paquet python avec `pip` peut provoquer une compilation et donc nécessiter des outils adéquats sur la machine. Ce n'est pas le cas avec Anaconda/Miniconda.

## Initialisation du projet
> [!CAUTION]
> :warning: **Les étapes de cette section ne sont à exécuter que lors de la première utilisation du projet**.

### Création et activation de l'environnement
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  python3 -m venv .in200
  source .in200/bin/activate
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda env create
  conda activate in200
  ```

### Installation des dépendances
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  python -m pip install -r requirements.txt
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)

  L'installation des dépendances est faite en même temps que la création de l'environnement.

## Utilisation du projet
### Activation de l'environnement
* Avec la distribution [python.org](https://www.python.org/)
  ```bash
  source .in200/bin/activate
  ```
* Avec la distribution [Anaconda](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)
  ```bash
  conda activate in200
  ```

### Exécuter le projet
```bash
python main.py
```

### Exécuter les tests
```bash
python tests/test_fizzbuzz.py
```

### Valider le code du projet (_linter_)
La validation utilise l'outil [ruff](https://docs.astral.sh/ruff/).

```bash
python -m ruff check .
```

### Reformater les fichiers
Le reformatage utilise également l'outil [ruff](https://docs.astral.sh/ruff/).

```bash
python -m ruff format .
```

### Valider les types (_static type checker_)
La vérification des types utilise l'outil [mypy](https://mypy-lang.org/index.html).
```bash
python -m mypy modules/fizzbuzz.py
```

## Notes sur [Visual Studio Code](https://code.visualstudio.com/)/[Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Pour sélectionner l'interpréteur ou l'environnement Python adéquat, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Python: Select Interpreter*.
* Pour ouvrir un REPL Python dans l'environnement courant, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Python: Start REPL*.
* Pour ouvrir un terminal dans l'environnement courant, il faut ouvrir la *Command Palette* (`Ctrl+Shift+P`), puis taper *Terminal: Create New Integrated Terminal*.
