import time

start = input('Iniciar cronometro y/n:')
if start == "y":
    a = time.time()
    global start_time
    start_time = a
    print("Tempo 0:", a)
else:
    print("ssss")

finish = input("Terminar? y/n: ")
if finish == "y":
    b = time.time()
    global finish_time
    finish_time = b


calculate = input("Calcular? y/n: ")
if calculate == "y":
    print("Tempo decorrido em segundos tendo como base tempo 0 =", a, "Tempo decorrido =", (b - a))

