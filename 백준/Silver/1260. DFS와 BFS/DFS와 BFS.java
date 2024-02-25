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

    private static class Point{
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n,m,v;
    static List<List<Integer>> g;
    static List<Integer> res = new ArrayList<>();
    static boolean[] visited;
    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        g = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g.get(a).add(b);
            g.get(b).add(a);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(g.get(i));
        }

        res = new ArrayList<>();
        visited = new boolean[n+1];
        DFS(v);
        for (Integer data : res) {
            System.out.print(data + " ");
        }
        System.out.println();
        res = new ArrayList<>();
        BFS(v);
        for (Integer data : res) {
            System.out.print(data + " ");
        }
    }

    public static void DFS(int v) {
        visited[v] = true;  // ! 방문 처리 후
        res.add(v);  // ! 순번에 넣어두기

        for (Integer node : g.get(v)) {
            if (!visited[node]) {
                visited[node] = true;
                DFS(node);
            }
        }
    }

    public static void BFS(int v) {
        Deque<Integer> dq = new ArrayDeque<>();
        boolean[] visited = new boolean[n + 1];
        visited[v] = true;
        res.add(v);
        dq.offer(v);
        // ! 시작 세팅 완료
        while (!dq.isEmpty()) {
            Integer now = dq.poll();

            for (Integer node : g.get(now)) {
                if (!visited[node]) {
                    visited[node] = true;
                    res.add(node);
                    dq.offer(node);
                }
            }
        }

    }

}