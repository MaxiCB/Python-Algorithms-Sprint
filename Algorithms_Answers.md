#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The running time of this snippet is Linear 0(n) - while a < n3 (n cubed) we add n2 (n squared) to a
The function in essence id doing (n2 * n) which is equal to n3 so the amount of times it runs is equal
to n

b) The running time of this snippet is Linear 0(n) - the function depends on for i in range(n) which will
run n times


c) The running time of this snippet is Linear 0(n) - this function will recurse until bunnies = 0
bunnies will always reach 0 after n operations. return 2 + bunnyEars(bunnies-1) will happen at the same
rate of the input

## Exercise II

To determine the floor while also reducing amount of eggs broke, I would divide the number of stories to get the middle floor.
I would then drop a egg, if the egg breaks I would go to the middle of the lower half, it the egg did not break I would go to 
the middle of the upper half. 

floor_count = num of floors

middle = floor_count / 2
drop_egg()
if egg != broken
    move to top half
else
    move to bottom half
    
The runtime complexity of this would be O(logN)
