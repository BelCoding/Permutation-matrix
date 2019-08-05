#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:35:51 2019

@author: Beltran Rodriguez
"""

def dec_to_bin(x, M):
    binary = []
    bin_str = str(bin(x)[2:])
    #print(x, bin_str, len(bin_str))
    ceros = M - len(bin_str)
    for i in range(ceros):
        binary.append(None)   

    for i in range(M-ceros):
        binary.append(int(bin_str[i]) == 1) 

    return binary


def is_permutation_matrix(A, M):
  # print(A)
   for i in range(M):
       if A[i][:].count(True) != 1 or [row[i] for row in A].count(True) != 1:
           return 0
   return 1


# Columns is a vector that only contains the indexes of the columns which bitvalue is 1.
def is_permutation_columns(columns, M):
# print(A)
# Check that there is not a repeated numbers, (means that a 1 was found more than 1 time on that column)
# We also check that every colunm index is in the list only one time

    for i in range(M):        
        s=0
        for ii in range(M):
            #if columns[i] == columns[ii] and i != ii:
            #   return 0 
            # We also check that every colunm index is in the list only one time
            if i == columns[ii]:
               s+=1
        if s != 1:
            return 0
        
    return 1



def testcase(M):
   # print(M)
    OnesColumnsCounter = []
    result = 1 # We first suppose hat the Matrix is permutable, then looking for ones in rows and columns we try to discard this.
    # When result turns to 0. We stop calculations, already decided that is not permutable matrix. But It continues reading the input
    
    # max_bin = 2**M-1
    # print("max_bin ", max_bin, 2**M, M)
    for x in range(M):
        input_number = int(input())
        if input_number > 2**M:
            print("Decimal number given not valid for the Range of the matrix, which has to fit on the binary representation")
            return 1
        
        mod = input_number % 2
        if mod > 0 and input_number > 1:
            result = 0 # All the decimal Odds numbers > 1 will have a representation in binary that contains more than one 1 in the row.
        else:
            vector = dec_to_bin(input_number, M)
            for i in range(len(vector)):
                if vector[i] == 1:
                    OnesColumnsCounter.append(i) # list of column indexes where we find a one.
            if vector.count(True) != 1:
                result = 0

    
   # print(result, OnesColumnsCounter)
   # If after checking the rows the matrix is not yet discarded we start checking the columns.
    if result == 1:
        print(is_permutation_columns(OnesColumnsCounter, M))
    else:
        print(0)
    

def main():
    # 1 < N < 100 and 0 < M < 10000.
    N = int(input()) # "Number of test cases: "
    if(N > 99):
        N=99
        
    for it in range(N):
        #print("Inputs:\n")
        M = int(input()) #size of the matrix
        if(M > 9999):
            M=9999
        if(M > 0):
            testcase(M)

if __name__ == '__main__':
    main()
