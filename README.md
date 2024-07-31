# ETL Project

Este projeto é um pipeline ETL simples utilizando MongoDB e Apache Airflow.

## Estrutura do Projeto

```plaintext
etl_project/
├── dags/
│   ├── etl_dag.py
├── data/
│   ├── raw/
│   ├── processed/
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── config/
│   ├── airflow.cfg
│   ├── mongo_config.py
├── requirements.txt
└── README.md
