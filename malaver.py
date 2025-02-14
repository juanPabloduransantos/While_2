#While_2

#input 


H = int(input("Digite su Numero: "))


#proccesing

Q = H/5
N = 0

while H>=Q:
    H = H-0.1*H
    N = N+1

# Output

print("Los rebotes desde el valor digitado en total son: "+str(N))