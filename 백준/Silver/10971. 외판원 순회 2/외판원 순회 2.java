import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[][] g;
    static int minDis = Integer.MAX_VALUE;
    static boolean[] visited;

    public static void DFS(int L, int sum, int v, int start) {
        if (L == n) { // ! n개의 도시를 모두 확인해서 돌아왔을 때
            int cnt = 0;
            for (int i = 1; i <= n; i++) {
                if (visited[i]) {
                    cnt += 1;
                }
            }
            if (cnt == n) { // 모두 방문한 경우
                if (g[v][start] != 0) {  // 시작점으로 다시 돌아올 수 있는 경우
                    minDis = Math.min(minDis, sum + g[v][start]);
                }
            }
        } else {
            for (int i = 1; i <= n; i++) {
                if (g[v][i] != 0 && !visited[i]) {  // 두 정점 연결되어 있는 경우
                    visited[i] = true;
//                    System.out.println("현재 노드 : " + v + " 현재 방문할 노드 : " + i);
                    DFS(L + 1, sum + g[v][i], i, start);
                    visited[i] = false;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        n = Integer.parseInt(br.readLine());
        g = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i <= n; i++) {
            visited = new boolean[n + 1];
            visited[i] = true; // 시작지점 방문처리 후 출발
            DFS(1, 0, i, i);
        }

        System.out.println(minDis);

    }
}