# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:02:16 2019

@author: Esdras
"""

import numpy as np
import json

L = 5 #Numero máximo de lotes
print("Lotes L =", L)
M = 10 #Numero de periodos
print("Periodos M =", M)

with open('crops.json', 'r') as f:
    crops_json = json.load(f)
    
crops_list = crops_json["crops"]

#print(crops_list[0]["name"])

def can_be_planted(crops_list, M, candidate_crop, prev_crop, period):
    #conditions
    belong_same_family_of_previous = crops_list[candidate_crop - 1]["family"] != crops_list[prev_crop - 1]
    have_enough_time_to_grow = crops_list[candidate_crop - 1]["grow_time"] <= (M - period)
    can_be_planted_in_period =  period in crops_list[candidate_crop - 1]["planting_period"]
    
    if belong_same_family_of_previous and have_enough_time_to_grow and can_be_planted_in_period:
        return True
    else:
        return False
    
#print(can_be_planted(crops_list, M, 1, 30, 1))

#cult = np.random.randint(1, 31, size=(M))

crops_period_1 = [1,2,9,10,11,15,16,18,19,22,23,30] #12
cult = np.array([]).astype(int)
#final_cults = np.array([]).astype(int)

period = 0
for k in range(L):
    cult_permutation = np.arange(1, 31)
    np.random.shuffle(cult_permutation)
    cult_permutation[0] = crops_period_1[np.random.randint(12)]
    cult = np.append(cult, [cult_permutation[0]])
    period = crops_list[cult_permutation[0] - 1]["grow_time"]
#    count_M = 0
    while period < M:
#        count = 1
        for j in range(1, M):
            if can_be_planted(crops_list, M, cult_permutation[j], cult_permutation[j-1], period):
                cult = np.append(cult, [cult_permutation[j]])
#                count+=1
                period += crops_list[cult_permutation[j] - 1]["grow_time"]
            if j == M-1:
                break
    print(cult)  
#    final_cults = np.concatenate(final_cults, [cult])


#                