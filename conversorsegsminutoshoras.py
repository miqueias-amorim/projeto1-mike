segundo_str = input("Por favor, coloque o número correspondente aos segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_rest = total_segs % 3600
minutos = segs_rest // 60
segs_rest_final = segs_rest % 60

print(horas, "horas, ", minutos, "minutos e", segs_rest_final, "segundos.")
