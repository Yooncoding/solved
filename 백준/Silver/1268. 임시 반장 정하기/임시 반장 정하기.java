import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[][] classInfo;
    static boolean[][] meetInfo;
    static BufferedReader br;
    static StringTokenizer st;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        classInfo = new int[n][5];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                classInfo[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        meetInfo = new boolean[n][n];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = j; k < n; k++) {
                    if (classInfo[j][i] == classInfo[k][i]) {
                        meetInfo[j][k] = true;
                        meetInfo[k][j] = true;
                    }
                }
            }
        }

        int maxCnt = 0;
        int maxStudent = 0;
        for (int currentStudent = 0; currentStudent < n; currentStudent++) {
            int currentCnt = 0;
            for (int i = 0; i < n; i++) {
                if (meetInfo[currentStudent][i]) {
                    currentCnt++;
                }
            }

            if (currentCnt > maxCnt) {
                maxCnt = currentCnt;
                maxStudent = currentStudent;
            }
        }
        System.out.println(maxStudent + 1);
    }
}
