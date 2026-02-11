def calcular_tamanyo(variable):
    tamanyo = 0
    try:
        tamanyo = len(variable)
    except:
        pass

    tamanyo = max(30, tamanyo)

    return tamanyo

def describe(variable):

    tamanyo = calcular_tamanyo(variable)

    print("┌", "─" * tamanyo, "┐", sep="")
    print("│", str(type(variable)).ljust(tamanyo), "│", sep="")
    print("│", str(variable).ljust(tamanyo), "│", sep="")
    print("└", "─" * tamanyo, "┘", sep="")
