# Python Package Template
✨🍰✨A template repository for Python package projects.

## Usage
### Initial setup
```shell
~$ bash scripts/setup.sh
Enter package name []: template-package
Enter package path [template-package]: tempate_pkg
Enter package description [Python package template description]: 
Enter package keywords (comma separated) [python]: python,template
Enter author name [Qi Zhao]: 
Enter author email [zhaoqi99@outlook.com]: 
Enter github username [Qi Zhao]: 

Package information:
Name: template-package
Description: Python package template description
Keywords: python,template
Github username: Qi Zhao
Author: Qi Zhao
Email: zhaoqi99@outlook.com

Confirm changes? [Y/n] 
Done. Please remember to modify 'install_requires' in 'setup.cfg'.
```

### Installation
```shell
~$ bash scripts/install.sh --dev # Install editable package
~$ bash scripts/install.sh
```

### Build
```shell
~$ bash scripts/build.sh # Build package distribution
```

### Publish
```shell
~$ bash scripts/publish.sh --dev # Upload to test PyPI
~$ bash scripts/publish.sh # Upload to PyPI
```

## License
[GNU General Public License v3.0](https://github.com/ZhaoQi99/python-package-template/blob/main/LICENSE)

## Author
* Qi Zhao([zhaoqi99@outlook.com](mailto:zhaoqi99@outlook.com))

## References
* [Installing Packages - Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)