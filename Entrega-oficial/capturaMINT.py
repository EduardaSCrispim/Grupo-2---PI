import psutil

from getmac import get_mac_address

import datetime

import csv

import time


def startProcess():

    print("""
    -------MINT: MONITORY AND INFRAESTRUCTURE TO X-RAY--------
    """)

    cpuUsuage = psutil.cpu_percent(interval=1)
    print(f"""
    
    Média de uso de CPU nos ultímos 10 segundos: {cpuUsuage}%""")

    freeDisk = 100 - psutil.disk_usage(path="/").percent
    print(f"""
    Disco rígido disponível: {freeDisk}% de 256 GB""")

    ramStats = psutil.virtual_memory()

    ramInUse = ramStats[2]

    freeRamPercent = float((100 - ramInUse))

    mac = get_mac_address()

    captureTime = datetime.datetime.now()

    rowResult = [cpuUsuage,ramInUse,freeRamPercent,mac,captureTime]

    print(f"""
    Uso de RAM: {ramInUse}%
    RAM disponível: {freeRamPercent:.1f}%
    Endereço de MAC da Máquina: {mac}

    Horário do monitoramento: {captureTime}
    """)

    with open('./relatorio.csv', 'a') as csvfile:
        csv.writer(csvfile).writerow(rowResult)

for i in range(15):
    startProcess()
    time.sleep(10)

