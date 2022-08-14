# Simple password gen
Password generator with support for KeePass [plugin]:https://keepass.info/plugins.html#convertto2xxml to convert to XML
## Installation
Install random
```bash
pip install random

pip install art
```
## Usage
```python
#Your email without domain
mail = list("YOUR EMAIL WITHOUT DOMAIN")

#Your email domain
mail = ''.join(mail) + "YOUR DOMAIN"
```
## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
