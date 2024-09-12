import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static Map<Integer, List<int[]>> routes;
    static int origin, destination;
    static int[] distance;
    static boolean[] visited;
    static BufferedReader br;
    static StringTokenizer st;


    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        routes = new HashMap<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            routes.putIfAbsent(a, new ArrayList<>());
            routes.get(a).add(new int[]{b, c});
        }

        st = new StringTokenizer(br.readLine());
        origin = Integer.parseInt(st.nextToken());
        destination = Integer.parseInt(st.nextToken());

        visited = new boolean[n + 1];
        distance = new int[n + 1];
        Arrays.fill(distance, (int) 1e9);
        distance[origin] = 0;

        for (int i = 0; i < n; i++) {
            int cityIndex = getNextCity();

            if (cityIndex == 0) break;

            visited[cityIndex] = true;

            if (routes.containsKey(cityIndex)) {
                for (int[] route : routes.get(cityIndex)) {
                    int ncityIndex = route[0];
                    int ncityCost = route[1];
                    distance[ncityIndex] = Math.min(distance[ncityIndex], distance[cityIndex] + ncityCost);
                }
            }
        }
        
        System.out.println(distance[destination]);
    }

    private static int getNextCity() {
        int minValue = (int) 1e9;
        int minIndex = 0;

        for (int i = 1; i <= n; i++) {
            if (!visited[i] && distance[i] < minValue) {
                minValue = distance[i];
                minIndex = i;
            }
        }

        return minIndex;
    }
}
