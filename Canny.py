'''
 np.polyfit函数：采用的是最小二次拟合，numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)，前三个参数是必须的
 '''


'''
np.ployld()
参数1表示：在没有参数2（也就是参数2默认False时），参数1是一个数组形式，且表示从高到低的多项式系数项，例如参数1为[4,5,6]表示：



 参数2表示：为True时，表示将参数1中的参数作为根来形成多项式，即参数1为[4,5,6]时表示：(x-4)(x-5)(x-6)=0，也就是：



 参数3表示：换参数标识，用惯了x，可以用 t，s之类的
 '''


'''
plt.plot(x,y,format_string,**kwargs)
x轴数据，y轴数据，format_string控制曲线的格式字串 

format_string 由颜色字符，风格字符，和标记字符 
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(300, 400, 20)
print(x,"\n")
y = x + np.random.randint(5,20,20)  # 随机取5到10中间20个数
poly = np.polyfit(x, y, deg=1)
print(poly)
z = np.polyval(poly, x)
print(z)
plt.plot(x, y,'bo',label='y')
plt.plot(x, z,'r',label='xy')

plt.legend()#将样例显示出来
# plt.plot()
plt.show()

