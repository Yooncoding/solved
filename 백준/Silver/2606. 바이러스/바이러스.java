import java.io.*;
import java.util.*;

public class Main {
    static int N, M, infectedCount;
    static boolean[] visited;
    static List<Integer>[] network;
    static BufferedReader br;
    static StringTokenizer st;
    
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        visited = new boolean[N + 1];
        network = new ArrayList[N + 1];
        infectedCount = 0;

        for (int i = 1; i <= N; i++) {
            network[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            network[a].add(b);
            network[b].add(a);
        }

        bfs(1);

        System.out.println(infectedCount - 1);
    }

    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            if (!visited[current]) {
                infectedCount++;
                visited[current] = true;
                for (int next : network[current]) {
                    if (!visited[next]) {
                        queue.add(next);
                    }
                }
            }
        }
    }
}
