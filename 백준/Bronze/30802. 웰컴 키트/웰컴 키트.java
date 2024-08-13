import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int n = Integer.parseInt(br.readLine());

    int[] arr = new int[6];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < 6; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    st = new StringTokenizer(br.readLine());
    int s = Integer.parseInt(st.nextToken());
    int p = Integer.parseInt(st.nextToken());

    int shirt = 0;
    for (int i = 0; i < 6; i++) {
      shirt += (arr[i] / s);
      if (arr[i] % s != 0) {
        shirt += 1;
      }
    }

    System.out.println(shirt);
    System.out.println(n / p + " " + n % p);
  }
}
