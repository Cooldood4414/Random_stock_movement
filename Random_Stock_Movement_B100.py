import numpy as np 

price = np.random.randint(-1,2,size=365) + 0.0001
total = np.sum(price) 
print(f'Total movement:${total:.2f}')
t_t = total + 100
print(f'Price: ${t_t:.2f}')