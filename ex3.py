while True:
    try:
        numero = int(input(" Entre an int número: "))
        print(5/numero)
        break
    except (ValueError,ZeroDivisionError):
        print("Valor Errado ou Não possso dividir por zero.")
    except:
        print("Não sei o que fazer...")