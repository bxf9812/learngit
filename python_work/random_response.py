import numpy as np
import matplotlib.pyplot as plt
 
def random_response_ages_adult(response):
    true_ans = response > 50
    if np.random.randint(0, 2) == 0:
        return true_ans
    else:
        return np.random.randint(0, 2) == 0

ages_adult = np.loadtxt("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", usecols=0, delimiter=", ")
total_count = len([i for i in ages_adult])
age_over_50_count= len([i for i in ages_adult if i > 50])
 
print(f'total_count={total_count}')
print(f'over_50={age_over_50_count}')
print(f'younger_than_or_equal_to_50={total_count-age_over_50_count}')
 
print('\nData perturbation')
perturbed_age_over_50_count = len([i for i in ages_adult if random_response_ages_adult(i)])
print(perturbed_age_over_50_count)
print(total_count-perturbed_age_over_50_count)

answers = [True if random_response_ages_adult(i) else False for i in ages_adult ]
def random_response_aggregation_and_estimation(answers):

    false_yesses = len(answers)/4
    total_yesses = np.sum([1 if r else 0 for r in answers])
    true_yesses = total_yesses - false_yesses
    rr_result = true_yesses*2
    return rr_result
 
estimated_age_over_50_count = random_response_aggregation_and_estimation(answers)
print('\nData aggregation and estimation')
print(int(estimated_age_over_50_count))
print(total_count-int(estimated_age_over_50_count))