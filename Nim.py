#Jogo do Nim

def computador_escolhe_jogada(n,m):
    k=1
    while k<=m:
        if (n-k)%(m+1)==0:
            return k
        else:
            k+=1
    else:
        return m
    
def usuario_escolhe_jogada(n,m):
 c=int(input("Entre com sua jogada: "))
 while m<c or c<=0:
  c=int(input("Valor incorreto. Entre com sua jogada novamente: "))
 else:
     return c

def partida():
 a= int(input("Entre com o número inicial: "))  
 b= int(input("Entre com o número máximo possível: "))
 while a<=b:
    a= int(input("Entre com o número inicial novamente: "))  
    b= int(input("Entre com o número máximo possível novamente: "))
 else:
   
     if a%(b+1)==0:
      print("Você começa!")

      while a>b :

       w=usuario_escolhe_jogada(a,b)
       a = a-w
       
       
       print(w, a)
       z=computador_escolhe_jogada(a,b)
       a= a-z
       
       print(z, a)
      else:
          if w==a:
              print("Você ganhou!")
              
          else:
              print("O computador ganhou!")
              

     else:
         print("Computador começa!")
         
         while a>b:
             z=computador_escolhe_jogada(a,b)
             a= a-z
             print(z, a)

             w=usuario_escolhe_jogada(a,b)
             a = a-w
             print(w, a)

         else:
             z= computador_escolhe_jogada(a,b)
         if z==a:
             print(4,0 ,"\nO computador ganhou!")
             
         else:
                 print("Você ganhou!")
         
def campeonato():
 a=0
 b=0
 m=1
 while m<=3:
      if partida() == "O computador ganhou!":
       a+=1
      else:
       b+=1
      
      m+=1
 else:
     print("Você: ", a ,"x", "Computador: ", b)
      
a= int(input("Quer jogar campeonato ou apenas uma partida? Digite 1 para partida e 2 para campeonato: "))
if a == 1:
  partida()
  print("Acabou!")
else:
  campeonato()
  print("Acabou!")
   
    

 
   
   





 
