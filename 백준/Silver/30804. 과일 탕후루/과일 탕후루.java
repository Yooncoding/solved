import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] fruits;
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        fruits = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            fruits[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for (int i = 1; i < 10; i++) {
            for (int j = i + 1; j < 10; j++) {
                int cnt = 0;
                for (int fruit : fruits) {
                    if (fruit == i || fruit == j) {
                        cnt++;
                    } else {
                        answer = Math.max(answer, cnt);
                        cnt = 0;
                    }
                }
                answer = Math.max(answer, cnt);
            }
        }
        System.out.println(answer);
    }
}

