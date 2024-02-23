import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

    /**
     * ! 모든 섬 연결.
     * ! 조건 : 환경 부담금 : e * L^2
     * ! 환경 부담금 최소로 지불, n개의 모든 섬 연결하도록
     * * 해당 문제 MST로 풀 수 있음
     * ! 모든 정점의 좌표가 주어지면 연결할 수 있는 모든 간선과 모든 비용을 계산한 후에 간선 리스트를 구현했어야 했음.
     */
    private static class Node implements Comparable<Node>{
        int index;
        long distance;

        Node(int index, long distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node node) {
            return Long.compare(this.distance, node.distance);
        }
    }
    static int T;
    static int n;
    static double e;
    static long[] tx,ty;
    static ArrayList<ArrayList<Node>> g;
    static PriorityQueue<Node> pq;
    static long res;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringTokenizer st2;

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());  // 정점 개수
            tx = new long[n];
            ty = new long[n];
            st = new StringTokenizer(br.readLine());
            st2 = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                tx[i] = Integer.parseInt(st.nextToken());
                ty[i] = Integer.parseInt(st2.nextToken());
            }
            e = Double.parseDouble(br.readLine());  // 세율
            g = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                g.add(new ArrayList<Node>());
            }
            // 거리 계산 후 노드 삽입
            calDis();
            // ! 프림 알고리즘
            res = 0;
            prim();
            System.out.println("#" + t + " " + Math.round(res * e));
        }
    }

    public static void calDis() {
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                long x = Math.abs(tx[i] - tx[j]);
                long y = Math.abs(ty[i] - ty[j]);
                long dis = x * x + y * y;
                g.get(i+1).add(new Node(j+1, dis));
                g.get(j + 1).add(new Node(i + 1, dis));
            }
        }
    }

    public static void prim() {
        pq = new PriorityQueue<>();
        pq.offer(new Node(1, 0));  // 임의의 정점 1번부터 시작
        boolean[] visited = new boolean[n + 1];

        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (!visited[now.index]) {
                visited[now.index] = true;
                res += now.distance;

                for (Node node : g.get(now.index)) {
                    if (!visited[node.index]) {
                        pq.offer(new Node(node.index, node.distance));
                    }
                }
            }
        }
    }
}