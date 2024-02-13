import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main {

    // ! n개의 노드, m개의 간선 (단방향)
    // ! 갔다가 돌아와야 함.
    // * n<= 10^3 -> O(N^2)까지 가능

    // ! 다른 모든 노드에서 x까지 모두 다익스트라를 사용하는 것이 아닌. 단방향 간선을 반대로 저장하여 목적지가 아닌 출발로 바꿔서 생각하면 된다.
    private static class Node implements Comparable<Node>{
        int index, distance;

        Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node node) {
            return this.distance - node.distance;
        }
    }
    static int n,m,x, INF = Integer.MAX_VALUE;  // ! x가 도착점. x가 갔다가 돌아가야 함.
    static ArrayList<ArrayList<Node>> g = new ArrayList<ArrayList<Node>>(); // 문제의 입력을 그대로 받은 g
    static ArrayList<ArrayList<Node>> reverse_g = new ArrayList<ArrayList<Node>>();  // 문제의 입력을 반대로 받은 reverse_g
    static int[] dis1, dis2;
    static int res;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<Node>());
            reverse_g.add(new ArrayList<Node>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            g.get(a).add(new Node(b, cost));
            reverse_g.get(b).add(new Node(a, cost));
        }
        dis1 = new int[n+1];
        dis2 = new int[n+1];
        Arrays.fill(dis1, INF);
        Arrays.fill(dis2, INF);

        dijkstra(x, dis1, g);
        dijkstra(x, dis2, reverse_g);

        solve();
    }

    public static void dijkstra(int start, int[] dis, ArrayList<ArrayList<Node>> g) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        dis[start] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.index;
            int distance = node.distance;

            if(distance > dis[now]) continue;

            for (Node adjNode : g.get(now)) {
                int cost = dis[now] + adjNode.distance;  // 인접노드까지 가는 비용
                if (cost < dis[adjNode.index]) {
                    dis[adjNode.index] = cost;
                    pq.offer(new Node(adjNode.index, cost));
                }
            }
        }
    }

    public static void solve() {
        for (int i = 1; i <= n; i++) {
            res = Math.max(dis1[i] + dis2[i], res);
        }
        System.out.println(res);
    }
}