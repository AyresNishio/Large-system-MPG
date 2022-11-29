import numpy as np
from random import seed
from random import sample

from f_observability import *


#def build_measurement_plan(Power_Sys,max_redun,semente = 5):


def build_empty_measurement_plan(Ybus, max_med):
    meas_plan = np.zeros([max_med,7],np.int32)
    

    n_bus = len(Ybus)
    measurement = 0
    #medidas de fluxo
    for line in range(n_bus):
        for column in range(n_bus):
            if(Ybus[line][column] == 1):
                de = line+1
                para = column+1
                meas_plan[measurement][0] = measurement+1
                meas_plan[measurement][1] = de
                meas_plan[measurement][2] = para
                meas_plan[measurement][3] = 1
                meas_plan[measurement][4] = 1
                meas_plan[measurement][5] = de
                meas_plan[measurement][6] = 0
                
                measurement = measurement + 1

    #medidas de injeção
    for line in range(n_bus):
        bus = line+1
        meas_plan[measurement][0] = measurement + 1
        meas_plan[measurement][1] = bus
        meas_plan[measurement][2] = bus
        meas_plan[measurement][3] = 1
        meas_plan[measurement][4] = 2
        meas_plan[measurement][5] = bus
        meas_plan[measurement][6] = 0
        
        measurement = measurement + 1

    return meas_plan

def add_random_measurement(meas_plan, possible_meas):
    chosen_meas = sample(possible_meas, 1)
    possible_meas = [bus for bus in possible_meas if bus not in chosen_meas]

    if meas_plan[chosen_meas[0]-1,6] == 0 : 
        meas_plan[chosen_meas[0]-1,6] = 1 
        return 1
    else :
        return 0

def remove_desactivated_measurements(meas_plan): #arquivo apenas com as medidas ativadas
    medidas_desativadas = []
    num_medidas_desativadas = 0
    cont = 0
    for line in meas_plan:
        if line[6] == 0:
            medidas_desativadas.append(cont)
            num_medidas_desativadas += 1
        cont = cont + 1

    #Deleta medidas da lista
    meas_plan = np.delete(meas_plan,medidas_desativadas, axis=0)
    #Corrige contagem inicial
    for i in range(meas_plan.shape[0]):
        meas_plan[i,0] = i + 1
    return meas_plan