import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;




public class Main {

    private static class Node implements Comparable<Node>{
        int index, distance;

        Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }

    static int n, m;
    static ArrayList<ArrayList<Node>> g = new ArrayList<ArrayList<Node>>();
    static int[] dis;
    static int INF = Integer.MAX_VALUE;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<Node>());
        }
        dis = new int[n + 1];
        Arrays.fill(dis, INF);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            g.get(a).add(new Node(b, c));
            g.get(b).add(new Node(a, c));
        }

        dijkstra(1);
        System.out.println(dis[n]);
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));  // 시작지점 세팅
        dis[start] = 0;

        while (!pq.isEmpty()) {  // 큐가 빌 때까지 반복
            Node node = pq.poll();
            int distance = node.distance;
            int now = node.index;

            if(distance > dis[now]) continue;

            for (Node adjNode : g.get(now)) {  // 현재 노드 인접 노드
                int cost = dis[now] + adjNode.distance;
                if (cost < dis[adjNode.index]) {
                    dis[adjNode.index] = cost;  // 최단 거리 갱신 후
                    pq.offer(new Node(adjNode.index, cost));
                }
            }
        }
    }
}