from datetime import datetime, timedelta
import os
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
import s3fs

def download_eod_to_minio():
    # Inizializza client Alpaca prendendo le chiavi dall'ambiente del container
    api_key = os.getenv('ALPACA_API_KEY')
    secret_key = os.getenv('ALPACA_SECRET_KEY')
    client = StockHistoricalDataClient(api_key, secret_key)
    
    # Paniere Multi-Asset
    assets = ["AAPL", "MSFT", "GOOGL", "NVDA"]
    
    # Richiesta dati ultimi 365 giorni
    request_params = StockBarsRequest(
        symbol_or_symbols=assets,
        timeframe=TimeFrame.Day,
        start=datetime.now() - timedelta(days=365),
        end=datetime.now()
    )
    
    bars = client.get_stock_bars(request_params)
    df = bars.df.reset_index()
    
    # Forziamo il formato delle date per evitare problemi
    df['timestamp'] = df['timestamp'].astype(str)
    
    # Salviamo direttamente su MinIO
    s3 = s3fs.S3FileSystem(
        key='minio_admin',
        secret='minio_password',
        client_kwargs={'endpoint_url': 'http://minio:9000'}
    )
    
    with s3.open('raw-data/alpaca_eod/market_data.csv', 'w') as f:
        df.to_csv(f, index=False)
        
    print(f"Scaricati con successo dati per {assets} e salvati su MinIO.")

with DAG(
    'alpaca_eod_ingestion',
    start_date=datetime(2026, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    fetch_data = PythonOperator(
        task_id='download_eod_to_minio',
        python_callable=download_eod_to_minio
    )