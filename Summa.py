#произведение элементов списка с нечетными номерами

def Summa(List):
    Sum = 0
    for i in range(1, len(List), 2):
        Sum += List[i]
    return Sum


