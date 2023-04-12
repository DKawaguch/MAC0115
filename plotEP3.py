# EP3 - plot
# Autor - Gabriel Morete
# Manual - https://matplotlib.org/stable/users/index

import matplotlib
from matplotlib import pyplot as plt

name = str(input("Nome do arquivo com os dados: "))

data = [[] for _ in range(6)]

# leitura dos dados
szl = -1
with open(name) as fle:
	for line in fle:
		d = list(map(float, (line.strip()).split(' ')))
		cszl = len(d)

		if szl == -1:
			szl = cszl

		if szl != cszl or cszl & 1:
			print("Arquivo " + name + " é inválido -- Abortar")
			exit(1)

		for j in range(0, len(d)):
			data[j].append(d[j])

# cores dos corpos
color = ["Blue", "Red", "Green"]

# desenha os corpos
for i in range(0, cszl//2):
	plt.scatter(data[2 * i], data[2 * i + 1], s = .1, color = color[i], label = "Corpo " + str(i + 1)) # desenha o corpo 1

# plt.xlim([-1 * (10**11), 1 * (10**11)]) # define as dimensões do eixo x
# plt.ylim([-1.25 * (10**11), 1.25 * (10**11)]) # define as dimensões do eixo y
# matplotlib.pyplot.gcf().set_size_inches(10.5, 12.5) # define o tamanho das imagens

plt.legend() # coloca legenda
# plt.axis('off')  # omite os eixos
plt.savefig(name+".png") # salva a figura, se quiser mudar o formato o python resolve
