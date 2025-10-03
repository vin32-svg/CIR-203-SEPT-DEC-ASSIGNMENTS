import numpy as np;
transactions=np.array([[3000,5000,4500,7500,5060,1000],
                          [6700,5600,7699,5666,6700,6000],
                          [5600,7500,6700,8800,7889,7600],
                          [5600,7500,8700,9500,7500,6900]])
print(transactions)
total_transaction_per_branch=np.sum (transactions, axis=1)

print("total_transaction_per_branch:",total_transaction_per_branch)
highest_transaction=np.max(transactions,axis=1)
print("highest_transaction:",highest_transaction)
average_monthly = transactions.mean()
print("Average monthly transaction volume (all branches):", average_monthly)
reshaped = transactions.reshape(3, 8)
print("Reshaped array (3x8):\n", reshaped)


