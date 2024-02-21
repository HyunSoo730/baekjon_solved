import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int T,n,m;   // n개의 노드, m개의 간선
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
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            parent = new int[n+1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
            }
            sb = new StringBuilder();
            System.out.print("#" + t + " ");
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int oper = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if(oper == 0) unionParent(a, b);
                else if (oper == 1) {
                    if (findParent(a) == findParent(b)) {
                        System.out.print(1);
                    } else {
                        System.out.print(0);
                    }
                }
            }
            System.out.println();
        }
    }
}