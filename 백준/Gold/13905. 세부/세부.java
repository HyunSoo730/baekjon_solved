import org.w3c.dom.Node;

import java.awt.*;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    private static class Edge implements Comparable<Edge>{
        int nodeA, nodeB;
        long distance;

        Edge(int nodeA, int nodeB, long distance) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.distance = distance;
        }

        @Override
        public int compareTo(Edge edge) {
            return Long.compare(edge.distance, this.distance);
        }
    }
    static int n, m;
    static List<Edge> edges = new ArrayList<>();
    static int[] parent;

    public static int findParent(int x) {
        if(x == parent[x]) return x;
        return parent[x] = findParent(parent[x]);
    }

    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if(a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long cost = Integer.parseInt(st.nextToken());
            edges.add(new Edge(a, b, cost));
        }

        // ! 유니온파인트 세팅
        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        Collections.sort(edges);  // 최대 비용으로 정렬
        long res = 0; // ! 초기값을 0으로 설정해줬어야 했음.
        // ! 간선의 비용이 최대값인 것부터 돌면서 연결되는 순간 가중치의 최소값이 최대화가 되는 시점
        for (Edge edge : edges) {
            int nodeA = findParent(edge.nodeA);
            int nodeB = findParent(edge.nodeB);
            if (nodeA != nodeB) {
                unionParent(nodeA, nodeB);
            }
            if (findParent(start) == findParent(end)) {
                res = edge.distance;
                break;
            }
        }

        System.out.println(res);
    }
}