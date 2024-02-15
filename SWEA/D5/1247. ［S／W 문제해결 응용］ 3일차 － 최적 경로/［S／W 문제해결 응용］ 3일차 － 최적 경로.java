import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Data{
    int x;
    int y;

    Data(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
public class Solution {

    static int T, n, minDis = Integer.MAX_VALUE;
    static Data person, home;
    static Data[] customers;
    static Data[] res;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            person = new Data(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            home = new Data(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            customers = new Data[n];
            for (int i = 0; i < n; i++) {
                customers[i] = new Data(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }
            visited = new boolean[n];
            // 순열로 순서마다 확인
            minDis = Integer.MAX_VALUE;
            DFS(0, person, 0);

            sb.append("#" + t).append(" ").append(minDis).append("\n");
        }
        System.out.println(sb);

    }

    public static void DFS(int L, Data prev, int sum) {
        if (sum >= minDis) {
            return;
        }
        if (L == n) {  // 모두 확인
            sum += cal(prev, home);
            if (sum < minDis) {
                minDis = sum;
            }
        } else {
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    DFS(L + 1, customers[i], sum + cal(customers[i], prev));
                    visited[i] = false;
                }
            }
        }
    }

    public static int cal(Data A, Data B) {
        return Math.abs(A.x - B.x) + Math.abs(A.y - B.y);
    }


}