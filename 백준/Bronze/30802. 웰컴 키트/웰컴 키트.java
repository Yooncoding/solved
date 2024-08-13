import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt();

    int[] arr = new int[6];
    for (int i = 0; i < 6; i++) {
      arr[i] = scanner.nextInt();
    }

    int s = scanner.nextInt();
    int p = scanner.nextInt();

    int shirt = 0;
    for (int i = 0; i < 6; i++) {
      shirt += (arr[i] / s);
      if (arr[i] % s != 0) {
        shirt += 1;
      }
    }

    System.out.println(shirt);
    System.out.println(n / p +" "+ n % p);
  }
}