import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    /**
     * ! n개의 정수.
     * ! 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 구하기.
     * ! 연속된 인덱스 선택 ?
     * ! 연속적으로 선택한 수의 합이 최댓값이 되는 수. -> 즉 메모이제이션은 이전까지 탐색했던 값과 현재 위치의 값을 비교하여 큰 값을 저장하면 된다.
     * * dp[i]는 i번째 인덱스까지의 최댓값이 저장되어 있다는 의미
     * * 예를들어 dp[3]은 dp[0] ~ dp[3]에서 연속으로 선택한 부분 수열의 최댓값이 저장되어 있다는 의미
     * ! DP문제 느낌이 난다면 일단 적어보면서 규칙을 찾아내야 한다.
     * ! 일단 이 문제에서 간과한 것이 dp[n]에 최대값이 저장될 것이라고 착각했다. dp를 풀 때 그렇게 생각하지 말자. dp 테이블 어딘가에 원하는 값이 있을 것이라고 생각하고 접근
     */
    static int n;
    static int[] data, dp;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        data = new int[n+1];
        dp = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        dp[1] = data[1];  // 자명한 값.
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1] + data[i], data[i]);
        }
        int max = Integer.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            max = Math.max(dp[i], max);
        }

        System.out.println(max);
    }

}