import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int m;
    static int b;
    static int[][] ground;
    static BufferedReader br;
    static StringTokenizer st;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        ground = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                ground[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int minTime = Integer.MAX_VALUE;
        int maxHeight = 0;

        for (int height = 0; height < 257; height++) {
            int timeCost = 0;
            int curBlock = b;

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < m; c++) {
                    if (ground[r][c] > height) {
                        timeCost += 2 * (ground[r][c] - height);
                        curBlock += ground[r][c] - height;
                    } else {
                        timeCost += height - ground[r][c];
                        curBlock -= height - ground[r][c];
                    }
                }
            }

            if (curBlock < 0) {
                continue;
            }

            if (minTime >= timeCost) {
                minTime = timeCost;
                maxHeight = height;
            }

        }
        
        System.out.println(minTime + " " + maxHeight);
    }
}


