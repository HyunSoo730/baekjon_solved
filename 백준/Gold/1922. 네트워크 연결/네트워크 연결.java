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
        int distance;

        Edge(int nodeA, int nodeB, int distance) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.distance = distance;
        }

        @Override
        public int compareTo(Edge ed) {
            return this.distance - ed.distance;
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
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            edges.add(new Edge(a, b, cost));
        }

        // ! 크루스칼 세팅 : 유니온파인드
        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] =i ;
        }

        Collections.sort(edges);
        int res = 0;
        for (Edge edge : edges) {
            int nodeA = findParent(edge.nodeA);
            int nodeB = findParent(edge.nodeB);
            if (nodeA != nodeB) {
                unionParent(nodeA, nodeB);
                res += edge.distance;
            }
        }

        System.out.println(res);
    }
}