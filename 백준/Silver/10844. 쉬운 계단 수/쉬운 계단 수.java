import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static long[][] dp;
    static long MOD = 1000000000;
    // ! dp[i][j] : i번째 자릿수가 j일때의 계단수
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        dp = new long[n + 1][10];

        for (int i = 1; i <= 9; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= 9; j++) {
                if(j == 0) dp[i][0] = dp[i-1][1] % MOD;  // ! 이전 자릿수가 1인 경우만 올 수 있잖아
                else if(j == 9) dp[i][9] = dp[i-1][8] % MOD; // ! 이전 자릿수가 8인 경우만 올 수 있잖아
                else{
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD;
                }
            }
        }

        long sum = 0;
        for (int i = 0; i <= 9; i++) {
            sum += dp[n][i];
        }

        System.out.println(sum % MOD);
    }
}