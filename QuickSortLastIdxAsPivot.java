
public class QuickSortLastIdxAsPivot {

    /* quick sort = moves smaller elements to left of a pivot. recursively divide array in 2 partitions.
    run-time complexity = Best case O(n log(n)), Average case O(n log(n)), Worst case O(n^2) if already sorted.
    space complexity = O(log(n)) due to recursion. **/
    public static void main(String[] args) {
        int[] numbers = Utility.fillArray().clone();

        System.out.println("before: ");
        Utility.printArray(numbers);

        //sorting algo
        quicksort(numbers);

        System.out.println("after: ");
        Utility.printArray(numbers);
    }

    private static void quicksort(int[] numbers) {
        quicksort(numbers, 0, numbers.length - 1);
    }

    private static void quicksort(int[] numbers, int lowIndex, int highIndex) {
        if (lowIndex >= highIndex) {
            return;
        }
        int pivot = numbers[highIndex];
        int leftPointer = partition(numbers, lowIndex, highIndex, pivot);
        quicksort(numbers, lowIndex, leftPointer - 1);
        quicksort(numbers, leftPointer + 1, highIndex);
    }

    private static int partition(int[] numbers, int lowIndex, int highIndex, int pivot) {
        int leftPointer = lowIndex;
        int rightPointer = highIndex;

        while (leftPointer < rightPointer) {
            //until we detect the number that is equal or larger than our pivot number,
            //we move forward moving the leftPointer to the right
            while (numbers[leftPointer] <= pivot && leftPointer < rightPointer) {
                leftPointer++;
            }

            while (numbers[rightPointer] >= pivot && leftPointer < rightPointer) {
                rightPointer--;
            }

            //swapping the larger than the pivot value with the smaller than the pivot value
            swap(numbers, leftPointer, rightPointer);
        }
        /*swapping the pivot with the larger value in the leftPointer position;
        so that the numbers smaller than the pivot are on the left side of it,
        and those larger than it, - on the right side of it.
         */
        if (numbers[leftPointer] > numbers[highIndex]) {
            swap(numbers, leftPointer, highIndex);
        } else {
            leftPointer = highIndex;
        }
        return leftPointer;
    }

    private static void swap(int[] array, int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }
}
