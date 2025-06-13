import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> a = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            a.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(a);

        for (int num : a) {
            System.out.println(num);
        }
    }
}
