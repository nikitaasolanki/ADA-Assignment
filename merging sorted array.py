# Python3 program to merge K
# sorted arrays
N = 4
 
# Merge and sort k arrays
def merge_and_sort(output, arr, n, k):
 
    # Put the elements in sorted array.
    for  i in range(k):
        for j in range(n):
            output[i * n + j] = arr[i][j];
 
    # Sort the output array
    output.sort()
 
# Driver Function
if __name__=='__main__':
 
    # Input 2D-array
    arr = [ [ 5, 7, 15, 18 ],
                     [ 1, 8, 9, 17 ],
                     [ 1, 4, 7, 7 ] ];
    n = N;
 
    # Number of arrays
    k = len(arr)
 
    # Output array
    output = [0 for i in range(n * k)]
    merge_and_sort(output, arr, n, k);
 
    # Print merged array
    for  i in range(n * k):
        print(output[i], end = ' ')
