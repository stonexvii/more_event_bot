from datetime import datetime


def on_start():
    current_time = datetime.now()
    current_time = current_time.strftime('%d/%m/%Y %H:%M:%S')
    print(f'Bot started at {current_time}')


def on_shutdown():
    current_time = datetime.now()
    current_time = current_time.strftime('%d/%m/%Y %H:%M:%S')
    print(f'Bot stopped at {current_time}')
