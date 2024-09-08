import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] group;
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        n = Integer.parseInt(br.readLine());

        group = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) {
                group[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }
                if (group[j][0] > group[i][0] && group[j][1] > group[i][1]) {
                    cnt++;
                }
            }
            answer[i] = cnt + 1;
            sb.append(answer[i]).append(" ");
        }
        System.out.println(sb.toString());
    }
}


