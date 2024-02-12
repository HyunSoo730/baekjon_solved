import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m;  // n개의 점, m개의 연결

    static int[] parent;

    public static int findParent(int x) {
        if(x == parent[x]) return x;
        return findParent(parent[x]);
    }

    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if(a<b) parent[b] = a;
        else parent[a] = b;
    }
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        parent = new int[n+1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        boolean cycle = false;
        int seq = 1;
        int res = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(cycle) continue;
            if (findParent(a) == findParent(b)) {
                cycle = true;
                res = seq;
            } else {
                seq+=1;
                unionParent(a, b);
            }
        }
        if (cycle) {
            System.out.println(res);
        } else {
            System.out.println(0);
        }
    }


}