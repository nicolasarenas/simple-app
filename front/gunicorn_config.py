import os

bind = f"{os.environ.get('APP_SERVER', '127.0.0.1')}:{os.environ.get('APP_PORT', '5001')}"
workers = 1  # Número de trabajadores, puedes ajustarlo según tus necesidades
accesslog = '-'  # '-' para stdout
errorlog = '-'  # '-' para stdout
