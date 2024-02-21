import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n, m;  // 사람의 수, 친구 관계의 수 -> 노드 개수, 간선 개수
    static ArrayList<ArrayList<Integer>> g = new ArrayList<>();
    static boolean[] visited;
    static boolean flag;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            g.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g.get(a).add(b);
            g.get(b).add(a);
        }
        for (int i = 0; i < n; i++) {
            visited = new boolean[n];
            visited[i] = true;  // 시작지점 방문처리 후 진행.
            DFS(1, i);
            if(flag) break;
        }
//        System.out.println(flag);
        System.out.println(flag ? 1 : 0);
    }

    public static void DFS(int L, int v) {
        if(flag) return;
        if (L == 5) {  // 모두 확인
            flag = true;
        } else {
            for (int node : g.get(v)) {
                if (!visited[node]) {
                    visited[node] = true;
                    DFS(L + 1, node);
                    visited[node] = false;
                }
            }
        }
    }
}