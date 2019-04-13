Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
<br>
<br>
I solved it by implementing: Genetic Algorithm(GA) and Hill Climbing(HC)
<br>
<br>
**Input file format:**<br>
The number of items<br>
The weights of the items(vector)<br>
The values of the items(vector)<br>
Knapsack capacity<br>
<br>
<br>
**Output file format:**<br>
The number of selected items<br>
Binary vector(1 if the item was selected, 0 otherwise)<br>
Value vector(value if the item was selected, 0 otherwise)<br>
Total value of the selected items<br>
