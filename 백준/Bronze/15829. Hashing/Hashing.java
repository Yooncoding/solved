import java.io.*;
import java.util.*;

public class Main {
    static int l;
    static String a;
    static int r = 31;
    static int m = 1234567891;
    static BufferedReader br;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        l = Integer.parseInt(br.readLine());

        a = br.readLine();

        long p = (long) Math.pow(r, 0);

        long sum = 0L;
        for (int i = 0; i < l; i++) {
            int n = a.charAt(i) - 96;
            sum += n * p % m;
            p = (p * r) % m;
        }
        System.out.println(sum%m);
    }
}
