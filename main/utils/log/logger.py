from datetime import datetime
time_list = []
log_list = []

class Logger:
    @staticmethod
    def log(step):
        print(f'\n{step}')
        log_list.append(f' {step}\n')
        time_list.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    @staticmethod
    def log_to_file():
        summary_list = list(zip(time_list, log_list))
        with open('../../../tests/log.txt', 'w', encoding='utf-8') as data:
            for item in summary_list:
                data.write(f'{item[0]}{item[1]}')

    @staticmethod
    def get_timings():
        return [*time_list]