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
        StringBuilder sb = new StringBuilder();
        for (int num : a) {
            sb.append(num).append('\n');
        }
        System.out.print(sb);
    }
}
