import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

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
            return Long.compare(this.distance, edge.distance);
        }
    }
    static int T, v,e;  // ! 정점 개수 v, 간선 개수 e
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
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= T; t++) {
            edges = new ArrayList<>();  // 매 순간 초기화
            st = new StringTokenizer(br.readLine());
            v = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                edges.add(new Edge(a, b, cost));
            }

            parent = new int[v + 1];
            for (int i = 1; i <= v; i++) {
                parent[i] = i;
            }
            
            Collections.sort(edges);
            long res = 0;  // 최소 비용

            sb.append("#").append(t).append(" ");
            int cnt = 0;
            for (Edge edge : edges) {
                int nodeA = findParent(edge.nodeA);
                int nodeB = findParent(edge.nodeB);
                if (nodeA != nodeB) {
                    unionParent(nodeA, nodeB);
                    res += edge.distance;
                }
            }
            sb.append(res).append("\n");
        }
        System.out.println(sb);
    }

}