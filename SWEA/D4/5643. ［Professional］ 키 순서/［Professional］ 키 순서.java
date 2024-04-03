import java.io.*;
import java.util.*;


/**
 * @author 조현수
 * @date 24.04.03
 * @link swea_5643_키 순서
 * @keyword_solution 현재 노드로부터 들어오는 간선, 나가는 간선 합이 n-1(본인의 제외한 노드 개수)와 같아야 현재 노드의 순위를 알 수 있음
 * 단순히 누가 누구 앞에 있다라고만 하는 것이 아니라 점들의 관계를 이용해 모든 점과 명확한 관계를 갖는 점을 찾아야 했음
 * 즉 모든 점과 연결할 수 있는 점을 찾아내면 끝
 * @input
 * @output
 * @time_complex
 * @perf 메모리 ~, 소요시간 ~
 */

public class Solution {
    static int T, n, m;
    static int[][] dist;
    static final int INF = 987654321;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            m = Integer.parseInt(br.readLine());

            // 초기화
            dist = new int[n + 1][n + 1];
            for (int i = 1; i <= n; i++) {
                Arrays.fill(dist[i], INF);
                dist[i][i] = 0;
            }

            // 입력
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                dist[a][b] = 1;
            }

            // Floyd-Warshall 알고리즘
            for (int k = 1; k <= n; k++) {
                for (int i = 1; i <= n; i++) {
                    for (int j = 1; j <= n; j++) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
            // 정답 계산
            int res = 0;
            for (int i = 1; i <= n; i++) {
                boolean flag = true;
                for (int j = 1; j <= n; j++) {
                    if (dist[i][j] == INF && dist[j][i] == INF) {
                        flag = false;
                        break;
                    }
                }
                if(flag) res += 1;
            }

            sb.append("#").append(t).append(" ").append(res).append("\n");
        }

        System.out.println(sb);
    }
}