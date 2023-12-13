#considering a scenario of a student who is given 2 assignments (a & b)
#both can take 1-5 & 2-6 hours respectively & completion of on assi. has no effect on the other
#the student can complete the assi. at any time within those intervals but 
#he has a practical lab after 9hr
#the probab that he will comp. his task before pract. lab is also given

import numpy as np
import matplotlib.pyplot as plt

sims = 100000

a = np.random.uniform(1, 5, sims)
b = np.random.uniform(2, 6, sims)

total_duration = a + b

plt.figure(figsize = (3, 1.5))
plt.hist(total_duration, density= True)
plt.axvline(9, color = 'r')
plt.show()
# the % of simulations that exceeded 9hr 
print((total_duration > 9).sum()/sims)
