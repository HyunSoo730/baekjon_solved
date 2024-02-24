import org.w3c.dom.Node;

import java.awt.*;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    private static class Node implements  Comparable<Node>{
        int index;
        long distance;
        Node(int index, long distance){
            this.index = index;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node node) {
            return Long.compare(node.distance, this.distance); // 오름차순 정렬
        }
    }
    static int n, m;
    static long INF = Long.MAX_VALUE;
    static long[] dis;
    static ArrayList<ArrayList<Node>> g = new ArrayList<>();


    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<Node>());
        }
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            g.get(a).add(new Node(b, cost));
            g.get(b).add(new Node(a, cost));
        }

        dis = new long[n+1];
        dijkstra(start);
        System.out.println(dis[end]);

    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, INF));
        dis[start] = INF;
        // ! 시작점 거리를 최대로 설정
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.index;
            long distance = node.distance; // 시작노드에서 현재 노드까지의 최대 거리

            if(distance < dis[now]) continue;

            for (Node adjNode : g.get(now)) {
                long cost = Math.min(dis[now], adjNode.distance); // 최대 거리 갱신 로직 변경
                if (cost > dis[adjNode.index]) {
                    dis[adjNode.index] = cost; // 갱신
                    pq.offer(new Node(adjNode.index, cost));
                }
            }
        }


    }
}