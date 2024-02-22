import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static int[] population;  // 각 구역의 인구 수, 선거구A, 선거구B
    static boolean[] visited;
    static ArrayList<ArrayList<Integer>> g;
    static int min = Integer.MAX_VALUE;
    static List<Integer> dataA, dataB;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        population = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            population[i] = Integer.parseInt(st.nextToken());
        } // 인구 수 입력
        g = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<Integer>());
        }

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            for (int j = 0; j < num; j++) {
                int node = Integer.parseInt(st.nextToken());
                g.get(i).add(node);  // ! i -> node 로 연결되어있다는 뜻
            }
        }

        visited = new boolean[n+1];
        DFS(1, 0);
//        System.out.println("최소 값 : " + min);
        if (min == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(min);
        }

    }


    public static void DFS(int L, int cnt) {
        if (L == n + 1) { // ! 1~n 모두 확인
            if(cnt == n || cnt == 0) return;
            dataA = new ArrayList<>();
            dataB = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                if(visited[i]) dataA.add(i);
                else dataB.add(i);
            }
            // 지역구 나눴음 -> 모두 연결되어 있는지 확인
            int cntA = BFS(dataA);
            int cntB = BFS(dataB);
            if (cntA == dataA.size() && cntB == dataB.size()) {
                // ! 검증됨 -> 최소 인구 수 구하기
                int sumA = 0;
                int sumB = 0;
                for(int idx : dataA) sumA += population[idx];
                for(int idx : dataB) sumB += population[idx];
                min = Math.min(min, Math.abs(sumA - sumB));
            }

        } else {
            visited[L] = true;  // 현재 인덱스 지역구A
            DFS(L + 1, cnt+1);
            visited[L] = false;
            DFS(L+1, cnt);  // 현재 인덱스 지역구B
        }
    }

    public static int BFS(List<Integer> data) {
        boolean[] visited = new boolean[n+1];
        Deque<Integer> dq = new ArrayDeque<>();
        visited[data.get(0)] = true;  // 시작점 방문철기
        dq.offer(data.get(0));

        int count = 1;  // 방문한 지역 개수
        while (!dq.isEmpty()) {
            int now = dq.poll();
            for (int node : g.get(now)) {
                if (data.contains(node) && !visited[node]) { // ! 선거구에 해당하고 아직 미방문
                    visited[node] = true;
                    dq.offer(node);
                    count += 1;
                }
            }
        }
        return count;
    }

}