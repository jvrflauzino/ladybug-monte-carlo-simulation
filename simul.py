import random
import matplotlib.pyplot as plt
random.seed(727)
def sim():
    pos = 12  #inicio na pos 12
    visitado = [False]*13  #0,1,2...12
    visitado[12] = True  #grafo num 12 ja visitado entao recebe valor true
    vistos = 1 #como o 12 eh o inicio ele ja foi visitado
    ultimo = None

    while vistos < 12: #todos os grafos precisam ser visitados
        pos = ((pos - 1 + random.choice((-1,1))) % 12) + 1 
        if not visitado[pos]: #se o grafo eh novo adiciona na lista
            visitado[pos] = True
            vistos += 1
            ultimo = pos
    return ultimo


N = 10000 #quantidade de simulacoes
count = 0
probs = []

#calcula a probabilidade do evento
for i in range(1, N+1):
    if sim() == 6:
        count += 1
    probs.append(count/i)

plt.plot(probs, label="Monte Carlo")
plt.axhline(1/11, color="red", linestyle="--", label="1/11")
plt.legend()
plt.xlabel("Simulacoes")
plt.ylabel("Probabilidade")
plt.title("Ladybug Random Walk")
plt.show()