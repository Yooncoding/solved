import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        scanner.close();

        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 1; i <= a; i++) {
            if (a%i == 0){
                list.add(i);
            }
        }

        if (list.size() <= b-1) {
            System.out.println(0);
        } else {
            System.out.println(list.get(b-1));
        }
    }
}