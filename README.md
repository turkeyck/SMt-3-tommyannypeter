# StatMech_Assignment3

## Problem 1: Properties of the van der Waals gas by computation 

1. Write a program to compute and plot *V* as a function of *P* at constant *T* for the van der Waals gas. 
2. Modify your program to include a comparison curve for the ideal gas law at the same temperature. 
3. Make plots for values of *T* that are at, above, and below *Tc*. 
4. For some values of temperature, the plots will have a peculiar feature. What is it? 
5. Make a plot of the chemical potential *μ* as a function of *P*. You might want to include a plot of *V* vs. *P* for comparison. <p>
   What does the plot of *μ* vs. *P* look like at, above, and below *Tc*? <p>
   The data you need to do a numerical integration of the Gibbs-Duhem relation is the same as you’ve already calculated for the first plot in this assignment. You just have to multiply the volume times the change in P and add it to the running sum to calculateμvs. P. 
