segsinput = input("Por favor, entre com o número de segundos que deseja converter: ")
totaldesegs = int(segsinput)

dias = totaldesegs // 86400
restosegs = totaldesegs % 86400
quanthoras = restosegs // 3600
restosegs2 = totaldesegs % 3600
minutos = restosegs2 // 60
quantsegsfinal = restosegs % 60

print(dias, "dias, ",quanthoras, "horas, ", minutos, "minutos e", quantsegsfinal, "segundos.")