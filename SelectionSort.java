
public class SelectionSort {

    /* 
    The time complexity of the selection sort algorithm is O(n²) which means it has a quadratic time complexity, 
    making it inefficient for large datasets. 
    Explanation: 
    Why O(n²)?: For an array of n elements, selection sort needs to iterate through all elements 
    to find the minimum value in the unsorted part, which requires n comparisons for each iteration. 
    Since this process repeats n-1 times (once for each element that needs to be placed in the sorted part), 
    the total number of comparisons becomes proportional to n². 
    
    Key points about selection sort complexity: 
    Worst case, average case, and best case are all O(n²):
    Regardless of the input data, selection sort always has a time complexity of O(n²). 
    
    Space complexity is O(1):
    Selection sort only requires a constant amount of extra memory, making it efficient in terms of space usage. 
    **/
    public static void main(String[] args) {
        int[] numbers = Utility.fillArray();

        System.out.println("before: ");
        Utility.printArray(numbers);
        long startTime = System.currentTimeMillis();

        selectionSort(numbers);

        long endTime = System.currentTimeMillis();
        System.out.println("after: " + (endTime - startTime) + "ms");
        Utility.printArray(numbers);
    }

    private static void selectionSort(int[] numbers) {
        int length = numbers.length;

        //as there is no chance to loop to the very last value/position,
        //there is nothing to swap it with and we know it is already where it goes,
        //so the last position too loop up for is length - 1
        for (int i = 0; i < length - 1; i++) {
            int min = numbers[i];
            int minValueIndex = i;
            for (int j = i + 1; j < length; j++) {
                if (numbers[j] < min) {
                    min = numbers[j];
                    minValueIndex = j;
                }
            }
            swap(numbers, i, minValueIndex);
        }
    }

    private static void swap(int[] numbers, int a, int b) {
        int temp = numbers[a];
        numbers[a] = numbers[b];
        numbers[b] = temp;
    }
}
