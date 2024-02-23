import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;

    /**
     * ! 연속으로 3잔을 마실 수는 없다. -> 이게 키 포인트
     * ! 이 문제의 핵심 중 하나는 현재 내가 잡은 포도주를 마시지 않고 넘겨도 된다는 것.
     * * 그렇다면 경우의 수는
     * * 1. 현재 포도주를 마시지 않음.
     * * 2. 현재 포도주를 마시고 이전 포도주를 마시지 않음.
     * * 3. 현재 포도주, 이전 포도주를 마시고, 그 이전 포도주는 마시지 않음
     * ! 위와 같은 3가지 경우가 존재하게 된다.
     * !ㅇ 왜 DP를 생각해야 했냐면 -> 현재 선택한 포도주가 다음 선택에서 영향을 끼치게 됨.
     */
    static int[] data, dp;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        data = new int[n+1];
        dp = new int[n+1];
        for (int i = 1; i <= n; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }
        // ! dp[i]는 i번째 까지 포도주를 확인한 결과 가장 많이 마실 수 있는 값
        dp[1] = data[1];
        if (n >= 2) { // 2잔인 경우 그냥 두잔 다 마시는게 최대
            // ! >=쓴 이유. n이 2 이상인 경우에 모두 적용해야 함.
            dp[2] = data[1] + data[2];
        }
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(Math.max(dp[i - 1], dp[i - 2] + data[i]), dp[i - 3] + data[i - 1] + data[i]);
        }
        System.out.println(dp[n]);
    }

}