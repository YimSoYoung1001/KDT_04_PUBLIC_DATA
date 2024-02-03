import matplotlib.pyplot as plt
import koreanize_matplotlib    #이거 없으면 한글이 다 깨지게 됨

plt.plot([-1, 0, 1, 2])
plt.title('그래프 제목', fontweight = 'bold')
plt.xlabel('간단 그래프')
plt.show()

