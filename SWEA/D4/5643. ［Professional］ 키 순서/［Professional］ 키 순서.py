import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T,n,m,a,b;
    static List<List<Integer>> g,reverse_g;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
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
                g.get(b).add(a);
                reverse_g.get(a).add(b);
            }

            int[] cnt = new int[n+1];
            int[] reverse_cnt = new int[n+1];

            for (int v = 1; v <= n; v++) {
                cnt[v] = BFS(v,g);
                reverse_cnt[v] = BFS(v, reverse_g);
            }

//            System.out.println(Arrays.toString(cnt));
//            System.out.println(Arrays.toString(reverse_cnt));

            int res = 0;
            for (int v = 1; v <= n; v++) {
                if (cnt[v] + reverse_cnt[v] == n - 1) {
                    res += 1;
                }
            }
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }

    public static int BFS(int v, List<List<Integer>> g) {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offer(v);
        boolean[] visited = new boolean[n+1];
        int cnt = 0;
        while (!dq.isEmpty()) {
            int now = dq.poll();
            for (Integer node : g.get(now)) {
                if (!visited[node]) {
                    visited[node] = true;
                    dq.offer(node);
                    cnt += 1;
                }
            }
        }
        return cnt;
    }


}