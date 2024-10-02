
import java.util.Random;

public class MergeSort {

    public static void main(String[] args) {
        //we are creating the random object to fill out our unsorted array
        Random rand = new Random();
        int[] numbers = new int[10];

        //loop through empty array slots and fill them out
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = rand.nextInt(10000000);
        }

        System.out.println("before: ");
        printArray(numbers);

        //sorting algo
        mergeSort(numbers);

        System.out.println("after: ");
        printArray(numbers);
    }

    //visual representation of the algorithm:
    //https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/600px-Merge_sort_algorithm_diagram.svg.png
    private static void mergeSort(int[] array) {
        int inputArrLength = array.length;

        if (inputArrLength < 2) {
            return;
        }

        //prepare divide part of divide and conquer
        int midIdx = inputArrLength / 2;
        int[] leftHalf = new int[midIdx];
        int[] rightHalf = new int[inputArrLength - midIdx];

        //populate both arrays
        for (int i = 0; i < inputArrLength; i++) {
            if (i < midIdx) {
                leftHalf[i] = array[i];
            } else {
                rightHalf[i - midIdx] = array[i];
            }
        }

        //and run mergeSort on each of divided arrays recursively
        mergeSort(leftHalf);
        mergeSort(rightHalf);
        mergeArrays(array, leftHalf, rightHalf);
    }

    private static void mergeArrays(int[] resultantArray, int[] leftHalf, int[] rightHalf) {
        int leftHalfSize = leftHalf.length;
        int rightHalfSize = rightHalf.length;

        int i = 0, j = 0, k = 0;
        //loop through both arrays to place the resultantArray with the properly ordered numbers
        while (i < leftHalfSize && j < rightHalfSize) {
            if (leftHalf[i] <= rightHalf[j]) {
                resultantArray[k] = leftHalf[i];
                i++;
            } else {
                resultantArray[k] = rightHalf[j];
                j++;
            }
            k++;
        }
        /* when we run out of elements in one of the arrays and there is still the leftover in another,
        we clean up and add all those elements in the end of the resultantArray
         */

        while (i < leftHalfSize) {
            resultantArray[k] = leftHalf[i];
            i++;
            k++;
        }

        while (j < rightHalfSize) {
            resultantArray[k] = rightHalf[j];
            j++;
            k++;
        }
    }

    private static void printArray(int[] array) {
        for (int item : array) {
            System.out.println(item);
        }
    }
}
