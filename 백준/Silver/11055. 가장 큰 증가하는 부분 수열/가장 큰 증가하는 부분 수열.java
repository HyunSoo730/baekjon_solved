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

    static long[] dp;
    static int[] data;
    static int n;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine()); // ! 해당 수가 가장 마지막에 올 떄의 합
        dp = new long[10001];
        data = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        dp[1] = data[1];
        // ! dp[i]는 i번째 값이 가장 마지막으로 올 때의 합
        for (int i = 2; i <= n; i++) {
            long max = 0; // ! 이전까지의 가장 큰 합
            for (int j = 1; j < i; j++) {
                if(dp[j] > max && data[j] < data[i]){  // ! 이전까지의 합 최대 && 현재 데이터보다 i번쨰 데이터가 더 큰 경우에만.
                    max = dp[j]; // ! 이전까지의 합 갱신
                }
            }
            dp[i] = max + data[i];
        }
        long maxData = 0;
        for (int i = 1; i <= n; i++) {
            maxData = Math.max(maxData, dp[i]);
        }
        System.out.println(maxData);
    }

}