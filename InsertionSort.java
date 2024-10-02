
public class InsertionSort {

    /*
    The time complexity of insertion sort is O(n^2) in the worst and average cases, 
    and O(n) in the best case;
    Worst case: The time it takes to sort a list is proportional to the square of 
    the number of elements in the list. This occurs when the input list is in decreasing order. 
    Average case: The time complexity is O(n^2).
    Best case: The time complexity is O(n). This occurs when the input array is already in sorted order.
    Insertion sort is a stable sorting algorithm that maintains the relative order of 
    equal elements. It's a simple and efficient algorithm for small input sizes or 
    partially sorted data.  **/

    public static void main(String[] args) {
        int[] numbers = Utility.fillArray().clone();

        System.out.println("before: ");
        Utility.printArray(numbers);

        insertionSort(numbers);

        System.out.println("after: ");
        Utility.printArray(numbers);
    }

    private static void insertionSort(int[] inputArray) {
        //we assume the first elem of the array is already sorted on itself,
        //so we start with the second elem/the 1st index
        for (int i = 1; i < inputArray.length; i++) {
            int currentValue = inputArray[i];
            //to stop moving back when we hit the beginning of the array
            int j = i - 1;
            //if the previous value in the array is larger than the current value put aside
            //we shift that greater value right by 1.
            while (j >= 0 && inputArray[j] > currentValue) {
                inputArray[j + 1] = inputArray[j];
                //putting the previous value into the next to it position, 
                //technically into the i position, where the currentValue is captured from
                j--; //moved 1 step back to check that value with the currentValue
            }
            //now put the currentValue in its correct position to the left
            inputArray[j + 1] = currentValue;
        }
    }
}
