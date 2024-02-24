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

    private static class Edge implements Comparable<Edge>{
        int nodeA, nodeB;
        int distance;

        Edge(int nodeA, int nodeB, int distance) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.distance = distance;
        }

        @Override
        public int compareTo(Edge edge) {
            return this.distance - edge.distance;
        }
    }
    static int n, m;
    static ArrayList<Edge> edges = new ArrayList<>();
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
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            edges.add(new Edge(a, b, cost));  // ! 간선 정보를 저장하기 때문에 애초에 하나를 넣으면 양방향이 된다.
        }
        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        // ! 핵심은 마을 분리를 어떻게 ? -> 모든 집들은 최소 비용으로 연결되어야 한다.
        Collections.sort(edges);
        long res = 0;
        int cnt = 0;
        int max = 0;
        for (Edge edge : edges) {
            int nodeA = findParent(edge.nodeA);
            int nodeB = findParent(edge.nodeB);
            if (nodeA != nodeB) {
                unionParent(nodeA, nodeB);
                res += edge.distance;
                max = edge.distance;
            }
        }

        System.out.println(res - max);
    }


}