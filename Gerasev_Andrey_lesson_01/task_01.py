duration = 2629743
seconds = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // (3600 * 24)
print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
