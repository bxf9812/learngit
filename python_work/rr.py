import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

def random_response_sex_adult(response):
    true_ans = response == 'Male'
    if np.random.binomial(1,0.8) == 0:  # 第一次0.2的概率为0 输出真实回答
        return true_ans
    else:
        return np.random.binomial(1,0.5) == 0 # 第二次 0.5概率随机返回回答

sex_adult = np.loadtxt("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", dtype=object, usecols=9, delimiter=", ")
total_count = len([i for i in sex_adult])
male= len([i for i in sex_adult if i == 'Male'])
 
print(f'total_count={total_count}')
print(f'male={male}')
print(f'female={total_count-male}')
print(f'male proportion1 = {male/total_count}')
 
perturbed_male = len([i for i in sex_adult if random_response_sex_adult(i)])
print('\nData perturbation')
print(f'male={perturbed_male}')
print(f'female={total_count-perturbed_male}')
print(f'male proportion2 = {perturbed_male/total_count}')

answers = [True if random_response_sex_adult(i) else False for i in sex_adult ]
def random_response_aggregation_and_estimation(answers):

    false_yesses = len(answers)*0.4
    total_yesses = np.sum([1 if r else 0 for r in answers])
    true_yesses = total_yesses - false_yesses
    rr_result = true_yesses*5
    return rr_result
 
estimated_male = random_response_aggregation_and_estimation(answers)
print('\nData aggregation and estimation')
print(f'male={int(estimated_male)}')
print(f'female={total_count-int(estimated_male)}')
print(f'male proportion3 = {int(estimated_male)/total_count}')


#relative_error = (int(estimated_male) - male)/male
#print(f'relative_error = {relative_error*100}%')
'''打印成表格'''
fig, ax =plt.subplots(1,1)
data=[[male,perturbed_male,int(estimated_male)],
      [total_count-male,total_count-perturbed_male,total_count-int(estimated_male)],
      [male/total_count,perturbed_male/total_count,int(estimated_male)/total_count]]
column_labels=["original", "noisy", "adjusted"]
df=pd.DataFrame(data,columns=column_labels)
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values,
colLabels=df.columns,
rowLabels=["male","female","male proportion"],
colWidths=[0.3,0.3,0.3],
rowColours =["yellow"] * 3,  
colColours =["yellow"] * 3,
loc="center")

plt.show()