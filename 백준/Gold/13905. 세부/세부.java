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
            return Long.compare(node.distance, this.distance);
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

    // ! 변형 다익스트라 -> 경로 상의 최소 가중치를 최대화 하는 경로를 찾아야함.
    // ! 시작점에서 각 노드까지 이동하는 경로 중 간선의 최소 가중치가 최대가 되는 경로 찾기.
    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, INF));
        dis[start] = INF;
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.index;
            long distance = node.distance; // 시작노드에서 현재 노드까지의 최대 거리

            if(distance < dis[now]) continue;
            // ! dis에는 최단거리 중 최대값이 들어가 있음
            for (Node adjNode : g.get(now)) {
                // ! 경로 상의 간선 가중치 중 최소값이 최대가 되도록 하는 경로를 찾는 문제.
                long cost = Math.min(dis[now], adjNode.distance);
                if (cost > dis[adjNode.index]) {
                    dis[adjNode.index] = cost; // 갱신
                    pq.offer(new Node(adjNode.index, cost));
                }
            }
        }


    }
}