
import java.util.Random;

public class Utility {

    public static int[] fillArray() {
        //we are creating the random object to fill out our unsorted array
        Random rand = new Random();
        int[] numbers = new int[10];

        //loop through empty array slots and fill them out
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = rand.nextInt(10000);
        }

        return numbers;
    }

    public static void printArray(int[] array) {
        for (int item : array) {
            System.out.println(item);
        }
    }
}
