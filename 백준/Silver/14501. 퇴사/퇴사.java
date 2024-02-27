import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static int[] time, price;
    static int max;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        time = new int[n+1];
        price = new int[n+1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            time[i] = Integer.parseInt(st.nextToken());
            price[i] = Integer.parseInt(st.nextToken());
        }

        DFS(1, 0);
        System.out.println(max);
    }

    public static void DFS(int L, int sum) {
        if (L == n+1) {  // ! 모든 인덱스 확인
            max = Math.max(max, sum);
        } else {
            if (L + time[L] <= n+1) {  // ! 현재 날짜에서 해당 상담의 시간을 사용해도 n+1 이하라면 가능
                DFS(L + time[L], sum + price[L]);  // 해당 상품 사용
            }
            DFS(L + 1, sum);  // 해당 인덱스 사용안하고 넘김
        }
    }
}