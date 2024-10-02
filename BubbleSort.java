
public class BubbleSort {

    /* 
    The bubble sort algorithm has a time complexity of O(n^2) in the average and worst cases, and a space complexity of O(1):
    Time complexity:
    Bubble sort's time complexity is O(n^2) in the average and worst cases. In the best case, when the list is already sorted, the time complexity is O(n).
    Space complexity:
    Bubble sort's space complexity is O(1), meaning it only requires a constant amount of additional memory. 
    Bubble sort is a simple, comparison-based algorithm that's easy to understand and implement. It's effective and efficient when the array is nearly sorted or has few elements. However, its slow speed can make it impractical for some applications, especially time-sensitive ones. 
    Here are some ways to improve the performance of bubble sort:
    Use a flag to track if any swaps were made in the inner loop. If no swaps were made, the array is already sorted.
    Only compare adjacent elements in the inner loop. 
    **/
    public static void main(String[] args) {
        int[] numbers = Utility.fillArray();

        System.out.println("before: ");
        Utility.printArray(numbers);

        //sorting algo
        boolean swapped = true;
        while (swapped) {
            swapped = false;
            for (int i = 0; i < numbers.length - 1; i++) {
                if (numbers[i] > numbers[i + 1]) {
                    swapped = true;
                    int temp = numbers[i];
                    numbers[i] = numbers[i + 1];
                    numbers[i + 1] = temp;
                }
            }
        }

        System.out.println("after: ");
        Utility.printArray(numbers);
    }
}
