import numpy as np 
import matplotlib.pyplot as plt
a = int(input('amount of simulations: '))
tm = 0 
pc = input('Do yo want to see a graph (y/n): ')
for i in range(a):
    price = np.random.randint(-1,2,size=365) + 0.001
    total = np.sum(price) 
    print(f'Total movement:${total:.2f}')
    t_t = total + 100
    print(f'Price: ${t_t:.2f}')
    print(f'This is the {i+1} simulation')
    if pc == 'y':
        plt.plot(t_t, marker='x', color='blue')
    if t_t > 100:
        tm += 1
    elif t_t < 100:
        tm -= 1
    print('Loss or gain in total sims', tm)
 
if pc == 'y': 
    plt.show()