# ARK Cli

This cli wraps the arkservers.net website.  The current features are:
* Display information about ark servers based on server name.
* Display currently logged in users for a server based on server address.

# Usage
```bash
ark-cli servers <search_query> #search servers by name
ark-cli players <server-address> #list active players
```

# Installation
```bash
pip install -e .
or
python setup.py install
or
make install install_rpms
```

# PhantomJS is required
```bash
sudo dnf install npm
sudo npm -g install phantomjs
```
