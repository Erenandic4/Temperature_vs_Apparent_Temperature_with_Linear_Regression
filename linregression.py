import numpy as np
import matplotlib.pyplot as plt 
def linreg(x,y):
    n=len(x)
    mean_of_x=np.mean(x)
    mean_of_y=np.mean(y)
    Var_x=np.sum((x-mean_of_x)**2)
    Cov_xy=np.sum(((y-mean_of_y)*(x-mean_of_x)))
    w=Cov_xy/Var_x
    b=mean_of_y-w*mean_of_x
    y_predict = w*x+b
    plt.scatter(x,y,marker='*',color='g')
    plt.plot(x,y_predict,color='red')
    plt.show()
    SS=np.sum((y_predict-mean_of_y)**2)/np.sum((y-mean_of_y)**2) 
    print("ACCURACY OF THE LINEAR REGRESSION IS: %.2f%%" %(SS*100))
    SSE = np.sum((y-y_predict)**2)  
    print("SUM OF SQUARED ERROR IS: %.2f" %(SSE))
    MSE = SSE / (n-2)
    print("MEAN SQUARE ERROR IS: %.2f" %(MSE))
