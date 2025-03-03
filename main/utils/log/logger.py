from datetime import datetime

class Logger:
    @staticmethod
    def log(step):
        print(step)
        log_step = f' {step}\n'
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('../../../artifacts/log.txt', 'a', encoding='utf-8') as data:
            data.write(f'{time_stamp}{log_step}')

    def error(step):
        print(step)
        log_step = f' {step}\n'
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('../../../artifacts/error_log.txt', 'a', encoding='utf-8') as data:
            data.write(f'{time_stamp}{log_step}')