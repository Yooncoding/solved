import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] points;
    static BufferedReader br;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        points = new int[n];
        for (int i = 0; i < n; i++) {
            points[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(points);
        int ex = (int) Math.round(n * 0.15);
        int[] slicedPoints = Arrays.stream(points, ex, n - ex).toArray();
        double sum = Arrays.stream(slicedPoints).sum();
        int answer = (int) Math.round(sum / (n - ex*2));
        System.out.println(answer);
    }
}
