def sum(a, b):
    try:
        r = a / b
        return print(r)
    except:
        print("Error: No momento algo deu errado, aguarde e tente novamente em alguns instantes.")
    finally:
        print("programa executado")

sum(100, "l") 