import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static int n,m, INF = Integer.MAX_VALUE;   // 노드, 간선
    static int[][] g;
    static int[] plan;
    // ! 플로이드 워셜로 문제 풀면 주의해야 할 것이 있다.
    // ! 문제의 입력에서 i에서 i로 가는 길은 없다고 입력이 들어오지만 가는 길이 없을 뿐 가지 못하는 것은 아니기 때문에 [i][i]는 1로 바꿔줘야 한다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        g = new int[n+1][n+1];
        plan = new int[m];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if(i==j)
                    g[i][j] = 1;  // ! 출발점과 도착점이 같은 경우도 여행이 가능해야 한다.
            }
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            plan[i] = Integer.parseInt(st.nextToken());
        }
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if(g[i][k] == 1 && g[k][j] == 1)
                        g[i][j] = 1;
                }
            }
        }
        boolean flag = true;
        for (int i = 0; i < m - 1; i++) {
            int start = plan[i];
            int end = plan[i + 1];
            if (g[start][end] == 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

}