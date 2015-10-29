# -*- coding: UTF-8 -*-

# Este ejemplo va a simular funciones lentas por medio del time.sleep

import cProfile
import time

def delay_loop(n):
    for i in range(n):
        time.sleep(0.1)

def delay1():
    delay_loop(10)

def delay2():
    delay_loop(10)

def delay3():
    delay_loop(10)

def simula_delay():
    delay1()
    delay2()
    delay3()

cProfile.run("simula_delay()")

# Descomentar para uso con runsnake

profile = cProfile.Profile()
profile.runcall(simula_delay)
profile.dump_stats('simula_delay.profile')
