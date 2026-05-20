def soma(a: int,b: int):
    """
    Função que soma dois parametros 
        args:
            - a (int): primeiro argumento. 
            - b (int): segundo  argumento. 
        return:
            (int) resultado da soma de dois numerais.
    """
    return a + b

a, b = int(input("Primeiro argumento: ")), int(input("Segundo argumento: "))

print(soma(a,b))
