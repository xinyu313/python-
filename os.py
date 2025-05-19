import os
import pandas as pd
#创建目录
os.makedirs(os.path.join('..','data'),exist_ok=True)
#创建csv文件路径
data_file=os.path.join('..','data','house_tiny.csv')
#写入内容
with open(data_file,'w') as f:
    f.write('Numrooms,Alley,Price\n')
    f.write('NA,Pave,127500\n')
    f.write('2,NA,10600\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,14000\n')
data=pd.read_csv(data_file)
print(data)


    