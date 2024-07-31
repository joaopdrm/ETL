# ETL Project

Este projeto implementa um pipeline ETL (Extract, Transform, Load) usando MongoDB e Apache Airflow. O pipeline extrai dados de arquivos CSV, transforma os dados conforme necessário e carrega os dados processados no MongoDB.

## Estrutura do Projeto

```plaintext
etl_project/
├── dags/
│   ├── etl_dag.py          # Definição da DAG do Airflow
├── data/
│   ├── raw/                # Dados brutos
│   ├── processed/          # Dados processados
├── scripts/
│   ├── extract.py          # Script de extração de dados
│   ├── transform.py        # Script de transformação de dados
│   ├── load.py             # Script de carregamento de dados
├── config/
│   ├── airflow.cfg         # Configurações do Airflow
│   ├── mongo_config.py     # Configurações do MongoDB
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto

## Requisitos
Certifique-se de ter os seguintes softwares instalados:

* MongoDB
* Apache Airflow
* Python 3.8+