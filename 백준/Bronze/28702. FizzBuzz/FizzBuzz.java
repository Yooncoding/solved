import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static StringBuilder sb;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        int result = 0;
        for (int i = 0; i < 3; i++) {
            String s = br.readLine();
            if (s.chars().allMatch(Character::isDigit)) {
                result = Integer.parseInt(s) + (3 - i);
            }
        }

        if (result % 3 == 0) {
            sb.append("Fizz");
        }
        if (result % 5 == 0) {
            sb.append("Buzz");
        }
        if (sb.length() == 0) {
            sb.append(result);
        }
        System.out.println(sb.toString());
    }
}
