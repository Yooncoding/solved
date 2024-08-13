import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] arr = new int[3];
        while (true) {
            arr[0] = scanner.nextInt();
            arr[1] = scanner.nextInt();
            arr[2] = scanner.nextInt();

            if (arr[0] == 0 && arr[1] == 0 & arr[2] == 0) break;

            Arrays.sort(arr);

            if (arr[2]*arr[2] == arr[1]*arr[1] + arr[0]*arr[0]) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}