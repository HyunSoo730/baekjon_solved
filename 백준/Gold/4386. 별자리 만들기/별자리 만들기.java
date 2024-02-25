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
        double distance;

        Edge(int nodeA, int nodeB, double distance) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.distance = distance;
        }

        @Override
        public int compareTo(Edge edge) {
            return Double.compare(this.distance, edge.distance);
        }
    }
    static int n;
    static int[] parent;
    static List<Edge> edges = new ArrayList<>();

    public static int findParent(int x) {
        if(x == parent[x]) return x;
        return parent[x] = findParent(parent[x]);
    }

    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if(a <b) parent[b] = a;
        else parent[a] = b;
    }


    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        double[] pointX = new double[n];
        double[] pointY = new double[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            double x = Double.parseDouble(st.nextToken());
            double y = Double.parseDouble(st.nextToken());
            pointX[i] = x;
            pointY[i] = y;
        }
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                double tx = Math.abs(pointX[i] - pointX[j]);
                double ty = Math.abs(pointY[i] - pointY[j]);
                double dis = Math.sqrt(tx * tx + ty * ty);
                edges.add(new Edge(i, j, dis));
            }
        }
        // ! 유니온 파인드 세팅
        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        Collections.sort(edges);
        double res = 0.0;
        for (Edge edge : edges) {
            int nodeA = findParent(edge.nodeA);
            int nodeB = findParent(edge.nodeB);
            if (nodeA != nodeB) {
                res += edge.distance;
                unionParent(nodeA, nodeB);
            }
        }

        System.out.println(Math.round(res * 100) / 100.0);

    }
}