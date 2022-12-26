# CLEAN ARCH IN PYTHON

Projeto criado com o intuito de aprender um pouco mais sobre a arquitetura limpa, sua estrutura, metodologia e aplicações


## HOW TO RUN THIS PROJECT:

- install all requirements
```shell
pip install -r requirements.txt
```
- on your python command line
```python
>>> from src.infra.config import *
>>> from src.infra.entities import *
>>> conn = DBConnectionManager()
>>> engine = conn.get_engine()
>>> Base.metadata.create_all(engine)
```

- run the tests
```shell
pytest -v -s
```
update: readme info to run the project