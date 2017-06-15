import matplotlib.pyplot as plt
ticks = [100, 200, 300, 400, 700, 1000, 1500, 2000, 4000]
shard1 = [18, 50, 65, 84, 145, 185, 265, 405, 718]
shard2 = [36, 80, 115, 170, 265, 395, 563, 747, 1595]
shard3 = [32, 70, 95, 115, 235, 306, 480, 700, 1385]
plt.xlabel('Numero de documentos')
plt.ylabel('Documentos en shard')
plt.plot(ticks, shard1, 'r', label='Shard 1')
plt.plot(ticks, shard2, 'g', label='Shard 2')
plt.plot(ticks, shard3, 'b', label='Shard 3')
plt.legend()
plt.savefig('shards.pdf')

