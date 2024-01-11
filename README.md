# Учебный проект на базе docker-compose

## Описание

С помощью Docker-compose разворачиваем среду из 4 контейнеров.

- Контейнер 1. PostgreSQL
- Контейнер 2. Spark – master
- Контейнер 3. Spark – worker1
- Контейнер 4. Spark – worker2
  
Источник данных – файл house_prices.csv

Схема обработки данных и взаимодействия контейнеров:

1) «Контейнер 1. PostgreSQL» запускается и создает (подключается к существующей) БД.
2) В БД подгружаются данные из файла house_prices в соответствующую таблицу.
3) «Контейнер 2. Spark – master» имеет возможность подключения к БД.
4) Контейнеры 2, 3 и 4 настроены как кластер Spark.
5) Приложение PySpark в виде файла my_spark.py загружено в «Контейнер 2. Spark – master». Его задача:
   
Из данных house_prices вывести информацию: Средние стоимости квартир и домов в зависимости от района и количества комнат.

## Запуск

```
docker build -t cluster-apache-spark:3.0.2 .
```

```
docker-compose up -d
```

```
/opt/spark/bin/spark-submit --master spark://spark-master:7077 \
--jars /opt/spark-apps/drivers/postgresql-42.7.1.jar \
--driver-memory 1G \
--executor-memory 1G \
/opt/spark-apps/main.py
```

## Технологии

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
