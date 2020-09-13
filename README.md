# prova-samba

Prova para admissão de desenvolvedor júnior da samba-tech. 

## Instalação do Ambiente
```
virtualenv --python python3.6 env
source env/bin/activate
```
```
pip install -r requirements.txt
```

## Variáveis de ambiente 
Para execução da API, as seguintes variáveis de ambiente devem ser configuradas:
```
DB_USER --> user do banco;
DB_PASS --> senha do banco;
DB_HOST --> host do banco;
DATABASE --> nome do schema.
```

## Execução 
```
python run.py
```


## Execução de testes unitarios
```
python unit_test/test.py
```


## Link Swagger

https://app.swaggerhub.com/apis/ViniciusBellagamba/prova-samba/1.0#/