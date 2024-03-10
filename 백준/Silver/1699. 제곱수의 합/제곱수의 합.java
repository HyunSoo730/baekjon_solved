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
    static long[] dp;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        dp = new long[100001];
        dp[1] = 1;
        // ! dp[i]는 i의 제곱수 합의 최소 개수
        for (int i = 2; i <= n; i++) {
            dp[i] = i; // ! 일단 최대값으로
            for (int j = 1; j * j <= i; j++) {
                if(dp[i] > dp[i-j*j]){
                    dp[i] = dp[i-j*j] + 1; // ! 여기서 1은 j*j를 사용한다는 뜻. 그렇기에 +1
                }
            }
        }
        System.out.println(dp[n]);
    }

}