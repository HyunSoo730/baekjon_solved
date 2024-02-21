import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] data, dp;
    static int res;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        data = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        dp = new int[n];
        dp[0] = 1;  // 자명한 사실
        res = 1;
        for (int i = 1; i < n; i++) {
            int max_length = 0;
            for (int j = 0; j < i; j++) {
                if (data[j] < data[i] && max_length < dp[j]) {
                    max_length = dp[j];
                }
            }
            dp[i] = max_length + 1;
            res = Math.max(res, dp[i]);
        }
        System.out.println(res);
    }
}