
  
chaine="abcdefghijklmnopqrstuvwxyz" * 10 
  

i=1 
  

while i <= len(chaine): 
	 
	print(chaine[:i]) 
  
	
	chaine=chaine[i:] 
  
	# On incrémente l'indice de croissance 
	i+=1 
# while