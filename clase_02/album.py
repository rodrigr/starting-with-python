# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:17:40 2019

@author: rodri
"""

# importando paquetes necesarios

import random

import numpy as np

# pruebas

x = random.random()

a = np.arange(10)

len(a)

a[:3]

random.shuffle(a)

np.mean(a)

random.randint(1, 10)

miSet = set()

miSet.add(1)
miSet.add(2)
miSet.update([1,4,5])
miSet.add(1)

#Primera simplificación

##1


figu = random.randint(1,6)

print("tu figurita es la número: % s" % (figu))

##2 

def comprar_figus():
    figu = random.randint(1,6)
    print("tu figurita es la número: % s" % (figu))
    return figu

def completar_album():
    album = set()
    figus_compradas = 0
    album_lleno = False
    while not(album_lleno):
        nueva_figu = comprar_figus()
        album.add(nueva_figu)
        album_lleno = len(album) == 6
        figus_compradas += 1
    print("compraste % s figuritas" % (figus_compradas))
    
completar_album()

##3
def comprar_figusII(n):
    figu = random.randint(1,n)
    print("tu figurita es la número: % s" % (figu))
    return figu

def completar_albumII(n):
    album = set()
    figus_compradas = 0
    album_lleno = False
    while not(album_lleno):
        nueva_figu = comprar_figusII(n)
        album.add(nueva_figu)
        album_lleno = len(album) == n
        figus_compradas += 1
    print("compraste % s figuritas" % (figus_compradas))
    
completar_albumII(350) 

##4

def comprar_figusIII(n):
    figu = random.randint(1,n)
    return figu

def completar_albumIII(n):
    album = set()
    figus_compradas = 0
    album_lleno = False
    while not(album_lleno):
        nueva_figu = comprar_figusIII(n)
        album.add(nueva_figu)
        album_lleno = len(album) == n
        figus_compradas += 1
    return figus_compradas
    
completar_albumIII(6)

Nrep = 1000
reps = list()

for i in range(Nrep):
    reps.append(completar_albumIII(6))
    
promedio = np.mean(reps)

#Caso Intermedio

##5

def promedio_figus(nRep, size):
    list_reps = list()
    for i in range(nRep):
        list_reps.append(completar_albumIII(size))
    return np.mean(list_reps)

promedio_figus(100,669)

#Con Paquetes

##6/7
def random_figu(album_size):
    figu = random.randint(1,album_size)
    return figu

def generar_pack(album_size,pack_size):
    pack = list()
    for i in range(pack_size):
        pack.append(random_figu(album_size))
    return pack

##8
def completar_albumIV(album_size,pack_size = 5):
    album = set()
    packs_comprados = 0
    album_lleno = False
    while not(album_lleno):
        nuevo_pack = generar_pack(album_size,pack_size)
        album.update(nuevo_pack)
        album_lleno = len(album) == album_size
        packs_comprados += 1
    return packs_comprados

##9
def promedio_packs(nRep, album_size, pack_size = 5):
    list_reps = list()
    for i in range(nRep):
        list_reps.append(completar_albumIV(album_size, pack_size))
    return np.mean(list_reps)

promedio_packs(100,669)

#Optativos

##10
def promedio_packsII(nRep, album_size, pack_size = 5):
    list_reps = list()
    for i in range(nRep):
        list_reps.append(completar_albumIV(album_size, pack_size))
    return list_reps

import seaborn as sns

sns.distplot(promedio_packsII(100,669))

x = promedio_packsII(100,669)

counter = 0

for i in x:
    if i <= 850: counter += 1
else:
    prob = counter/len(x)




