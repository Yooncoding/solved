import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> a = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            a.add(num);
        }

        int m = Integer.parseInt(br.readLine());
        List<Integer> b = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int num = Integer.parseInt(st.nextToken());
            b.add(num);
        }

        Collections.sort(a);
        for (int num : b) {
            int result = Collections.binarySearch(a, num);
            if (result >= 0) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }

    }
}
