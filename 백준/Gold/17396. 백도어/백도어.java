import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main {

    private static class Node implements Comparable<Node>{
        int index;
        long distance;

        Node(int index, long distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.distance, o.distance);
        }
    }
    static int n, m;
    static long INF = Long.MAX_VALUE;
    static int[] isSee;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<ArrayList<Node>> g = new ArrayList<ArrayList<Node>>();
    static long[] dis;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        isSee = new int[n];
        dis = new long[n];  // 최단거리 저장 배열
        for (int i = 0; i < n; i++) {
            isSee[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < n; i++) {
            g.add(new ArrayList<Node>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            g.get(a).add(new Node(b, cost));
            g.get(b).add(new Node(a, cost));  // 양방향
        }

        Arrays.fill(dis, INF);
        dijkstra(0);
        if (dis[n - 1] != INF) {
            System.out.println(dis[n - 1]);
        } else {
            System.out.println(-1);

        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        dis[start] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.index;  // 현재 노드 번호
            long distance = node.distance;  // 현재 노드까지의 거리

            if(distance > dis[now]) continue;
            for (Node adjNode : g.get(now)) {
                if(adjNode.index != n-1 && isSee[adjNode.index] == 1) continue;
                long cost = dis[now] + adjNode.distance;
                if (cost < dis[adjNode.index]) {
                    dis[adjNode.index] = cost;
                    pq.offer(new Node(adjNode.index, cost));
                }
            }
        }
    }


}