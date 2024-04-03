import java.io.*;
import java.util.*;


/**
 * @author 조현수
 * @date 24.04.03
 * @link swea_5643_키 순서
 * @keyword_solution  현재 노드로부터 들어오는 간선, 나가는 간선 합이 n-1(본인의 제외한 노드 개수)와 같아야 현재 노드의 순위를 알 수 있음
 * 단순히 누가 누구 앞에 있다라고만 하는 것이 아니라 점들의 관계를 이용해 모든 점과 명확한 관계를 갖는 점을 찾아야 했음
 * 즉 모든 점과 연결할 수 있는 점을 찾아내면 끝
 * @input
 * @output
 * @time_complex
 * @perf 메모리 ~, 소요시간 ~
 */
public class Solution {

    static int T, n, m, a, b;
    static ArrayList<ArrayList<Integer>> g, reverse_g;
    static int[] cnt, reverse_cnt;
    static StringBuilder sb = new StringBuilder();

    public static int BFS(int v, ArrayList<ArrayList<Integer>> g) {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offer(v); // ! 시작 노드

        int cnt = 0;
        boolean[] visited = new boolean[n + 1];
        visited[v] = true;
        while (!dq.isEmpty()) {
            int now = dq.poll();
            for (Integer next : g.get(now)) {
                if (!visited[next]) {
                    visited[next] = true;
                    cnt += 1;
                    dq.offer(next);
                }
            }

        }
        return cnt;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            m = Integer.parseInt(br.readLine());
            g = new ArrayList<>();
            reverse_g = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                g.add(new ArrayList<Integer>());
                reverse_g.add(new ArrayList<Integer>());
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                // a < b
                g.get(b).add(a);    // 진입차수
                reverse_g.get(a).add(b);  // 진출차수
            }

            // ! 개수 계산
            cnt = new int[n+1];
            reverse_cnt = new int[n+1];
            int res = 0;
            for (int  v = 1; v <= n; v++) {
                cnt[v] = BFS(v, g);
                reverse_cnt[v] = BFS(v, reverse_g);
                if (cnt[v] + reverse_cnt[v] == n - 1) {
                    res += 1;
                }
            }

            sb.append("#").append(t).append(" ").append(res).append("\n");

        }

        System.out.println(sb);

    }

}