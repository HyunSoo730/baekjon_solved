import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T;
    static int n;
    static int[] data, dp;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            data = new int[n + 1];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }

            dp = new int[n+1];

            for (int i = 1; i <= n; i++) {
                int max_length = 0;
                for (int j = i - 1; j >= 1; j--) {
                    if (data[i] > data[j] && dp[j] > max_length) {
                        max_length = dp[j];
                    }
                }
                dp[i] = max_length + 1;
            }
            int res = 0;
            for (int i = 1; i <= n; i++) {
                res = Math.max(res, dp[i]);
            }
            sb.append("#").append(t).append(" ");
            sb.append(res).append("\n");

        }
        System.out.println(sb);
    }
}