import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] arr;
    static BufferedReader br;
    static StringTokenizer st;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        double sum = 0;
        Arrays.sort(arr);

        for (int i = 0; i < n; i++) {
            sum += (double) arr[i] / arr[n - 1] * 100;
        }
        System.out.println(sum / n);
    }
}
