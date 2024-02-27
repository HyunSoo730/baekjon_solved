import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static class Node implements Comparable<Node>{
        int index;
        int distance;

        Node(int index, int distance) {
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node node) {
            return this.distance - node.distance;
        }
    }
    static int v,e;  // 정점 수, 간선 수
    static int INF = Integer.MAX_VALUE;
    static int[] dis;  // ! 최단경로 기록할 배열
    // ! 방향 그래프 최단경로 : 다익스트라
    static List<List<Node>> g = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken()); // ! 정점 개수
        e = Integer.parseInt(st.nextToken()); // ! 간선 개수

        int start = Integer.parseInt(br.readLine());

        for (int i = 0; i <= v; i++) {
            g.add(new ArrayList<Node>());
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            g.get(a).add(new Node(b, cost));
        }

        // 다익스트라
        dis = new int[v+1];
        Arrays.fill(dis, INF);
        dijkstra(start);
        for (int i = 1; i <= v; i++) {
            System.out.println(dis[i] == INF ? "INF" : dis[i]);
        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        dis[start] = 0;  // 시작점에서 시작점 0
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.index;
            int distance = node.distance;

            if(distance > dis[now]) continue;  // ! 기존 최단길이보다 크면 확인할 필요가 없음

            for (Node adjNode : g.get(now)) {  // ! 현재 노드의 인접노드들 확인
                int cost = dis[now] + adjNode.distance;  // ! 현재 노드까지의 비용 + now -> adjNode 로의 비용
                if (cost < dis[adjNode.index]) {
                    dis[adjNode.index] = cost;  // 비용 갱신 후
                    pq.offer(new Node(adjNode.index, cost));
                }
            }
        }
    }
}