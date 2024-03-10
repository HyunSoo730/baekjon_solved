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

    static int T, n, INF = 100001;
    static long[][] dp;
    static int[][] data;
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            n = Integer.parseInt(br.readLine());
            dp = new long[2][INF];
            data = new int[2][INF];

            for (int i = 0; i < 2; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    data[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            dp[0][0] = data[0][0];
            dp[1][0] = data[1][0];
            if(n >= 2){
                dp[0][1] = data[1][0] + data[0][1];
                dp[1][1] = data[0][0] + data[1][1];
            }
            for (int i = 2; i < n; i++) {
                dp[0][i] = Math.max(dp[1][i - 1], dp[1][i - 2]) + data[0][i];
                dp[1][i] = Math.max(dp[0][i - 1], dp[0][i - 2]) + data[1][i];
            }

            System.out.println(Math.max(dp[0][n - 1], dp[1][n - 1]));

        }
    }

}