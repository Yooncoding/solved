import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {
    static int n;
    static String[] words;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        Set<String> wordSet = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            wordSet.add(br.readLine());
        }

        words = wordSet.toArray(new String[0]);

        Arrays.sort(words, (word1, word2) -> {
            if (word1.length() != word2.length()) {
                return word1.length() - word2.length();
            } else {
                return word1.compareTo(word2);
            }
        });

        for (String word : words) {
            System.out.println(word);
        }
    }
}
