import org.w3c.dom.Node;

import javax.xml.crypto.Data;
import java.awt.*;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static long[][] dp;

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());
        dp = new long[10000][10];
        for (int i = 0; i < 10; i++) {
            dp[1][i] = 1;
        }
        // ! dp[i][j] : i번째 수에 j가 왔을 때의 오르막 수
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= 9; j++) {
                for (int k = 0; k <= j; k++) {
                    dp[i][j] += dp[i-1][k]%10007;
                }
            }
        }
        long sum = 0;
        for (int i = 0; i <= 9; i++) {
            sum += dp[n][i];
        }
        System.out.println(sum%10007);


    }

}