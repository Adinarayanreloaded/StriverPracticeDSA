#include<bits/stdc++.h>
using namespace std;

// Function to sort the array and return the largest element
int sortArr(vector<int>& arr) {
    // Sort the array in ascending order
    sort(arr.begin(), arr.end());
    
    // Return the last element (largest element) after sorting
    return arr[arr.size() - 1];
}

int main() {
    // Initialize arrays
    vector<int> arr1 = {2, 5, 1, 3, 0};
    vector<int> arr2 = {8, 10, 5, 7, 9};
   
    // Find and output the largest element in both arrays
    cout << "The Largest element in the array is: " << sortArr(arr1) << endl;
    cout << "The Largest element in the array is: " << sortArr(arr2);
   
    return 0;
}
____________________________________________________________________________________________________________________

import java.util.Arrays;

class Solution {

    // Function to sort the array and return the largest element
    public static int sortArr(int[] arr) {
        // Sort the array in ascending order
        Arrays.sort(arr);
        
        // Return the last element (largest element) after sorting
        return arr[arr.length - 1];
    }
}

public class Main {

    public static void main(String[] args) {
        // Initialize arrays
        int[] arr1 = {2, 5, 1, 3, 0};
        int[] arr2 = {8, 10, 5, 7, 9};
        
        // Find and output the largest element in both arrays
        System.out.println("The Largest element in the array is: " + Solution.sortArr(arr1));
        System.out.println("The Largest element in the array is: " + Solution.sortArr(arr2));
    }
}

__________________________________________________________________________________________________________________

# Function to sort the array and return the largest element
def sortArr(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Return the last element (largest element) after sorting
    return arr[-1]

# Driver code
if __name__ == "__main__":
    # Initialize arrays
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    
    # Find and output the largest element in both arrays
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))

