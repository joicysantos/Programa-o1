# coding: utf-8
# Programacao1 UFCG
# Instituicao ######
# Aluno-matricula
# nome do programa

quantidade_alunos = int(raw_input())
medias = [] # lista vazia, onde vai ser adicionado a media
aprovados = 0
total_turma = 0

for aluno in range(quantidade_alunos): 
	nota1 = float(raw_input())     #entradas de dados, responsaveis pelas notas de cada aluno
	nota2 = float(raw_input())
	nota3 = float(raw_input())

	media = float((nota1 + nota2 + nota3)) / quantidade_alunos
	medias.append(media)

for nota in medias:
	total_turma += nota
	
	if nota >= 8.0:
		aprovados += 1

maior = medias[0] 

for n in range(len(medias)):
	if medias[n] > maior:
		maior = medias[n]

media_turma = total_turma / quantidade_alunos

print "Quantidade de alunos aprovados: %d" %(aprovados) #SAIDA
print "Média da turma: %.1f" %(media_turma) #SAIDA
print "A maior média obtida: %.1f" %(maior) #SAIDA
	
