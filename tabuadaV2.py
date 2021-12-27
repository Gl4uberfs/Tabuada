print("***** TABUADA V2 *****")
#"Descrição, à tabuada mostrará os valores maiores que ZERO, não coloquei para mostrar os valores negativos."

while True:
    print("\n Pra sair digite valores menores que ZERO, ex:'-1'")
    n = int(input("Digite um valor para ver sua tabuada: "))
    if n < 0:
        break 
    print("=" * 30)
    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")

print("Encerrado!")