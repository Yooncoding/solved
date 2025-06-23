import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> queue = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();

            switch (cmd) {
                case "push":
                    queue.addLast(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    System.out.println(queue.isEmpty() ? -1 : queue.pollFirst());
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    System.out.println(queue.isEmpty() ? 1 : 0);
                    break;
                case "front":
                    System.out.println(queue.isEmpty() ? -1 : queue.peekFirst());
                    break;
                case "back":
                    System.out.println(queue.isEmpty() ? -1 : queue.peekLast());
                    break;
            }
        }
    }
}
