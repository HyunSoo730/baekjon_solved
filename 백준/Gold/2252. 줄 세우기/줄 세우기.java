import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    // * 노드의 개수 v와 간선의 개수 e
    // * 노드의 개수는 최대 100,000개라고 가정
    static int n,m;
    // 모든 노드에 대한 진입차수는 0으로 초기화
    static int[] indegree = new int[100001]; // 노드 개수만큼
    // 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    static ArrayList<ArrayList<Integer>> g = new ArrayList<ArrayList<Integer>>();

    // ! 위상 정렬 함수
    public static void topologySort() {
        ArrayList<Integer> res = new ArrayList<>(); // * 알고리즘 수행 결과를 담을 리스트
        Deque<Integer> dq = new ArrayDeque<>();

        // 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                dq.offer(i);
            }
        }

        // * 큐가 빌 때까지 반복
        while (!dq.isEmpty()) {
            // 큐에서 원소 꺼내기
            int now = dq.poll();
            res.add(now);
            // * 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for (Integer node : g.get(now)) {  // ! 여기서 node는 now(현재)꺼낸 노드의 인접 노드
                indegree[node] -= 1;
                // * 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if (indegree[node] == 0) {
                    dq.offer(node);
                }
            }
        }

        // ! 위상 정렬을 수행한 결과 출력
        for (int i = 0; i < res.size(); i++) {
            System.out.print(res.get(i) + " ");
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());  // ! 노드 개수
        m = Integer.parseInt(st.nextToken()); // ! 간선 개수
        // * 그래프 초기화
        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<Integer>());
        }

        // * 방향 그래프의 모든 간선 정보를 입력 받기
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g.get(a).add(b);   // ? 정점 a -> b로 이동 가능
            // ! 진입 차수 1 증가
            indegree[b] += 1;
        }
        topologySort();
    }
}