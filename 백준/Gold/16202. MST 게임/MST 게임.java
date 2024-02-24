import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    private static class Edge implements Comparable<Edge> {
        int nodeA, nodeB, distance;

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

    static int n, m, k;
    static List<Edge> edges = new ArrayList<>();
    static int[] parent;
    static int edgeCnt, res;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();
    static PriorityQueue<Edge> temp = new PriorityQueue<>();

    public static int findParent(int x) {
        if (x == parent[x]) return x;
        return parent[x] = findParent(parent[x]);
    }

    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
//            edges.add(new Edge(a, b, i+1));
            pq.offer(new Edge(a, b, i + 1));
        }
        boolean flag = true;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            temp = new PriorityQueue<>();
            kruskal();
            if(edgeCnt == n-1) sb.append(res + " ");
            else{
                sb.append("0 ".repeat(k - i));
                break;
            }
            temp.poll();
            pq = temp;
        }
        System.out.println(sb);


    }

    public static void kruskal() {
        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        res = 0;
        edgeCnt = 0;

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            int nodeA = findParent(edge.nodeA);
            int nodeB = findParent(edge.nodeB);
            if (nodeA != nodeB) {
                unionParent(nodeA, nodeB);
                res += edge.distance;
                edgeCnt += 1;
            }
            temp.offer(edge);
        }

    }



}