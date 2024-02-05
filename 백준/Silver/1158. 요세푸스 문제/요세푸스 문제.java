import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n,k;
    static Deque<Integer> dq = new ArrayDeque<>();
    static List<Integer> res = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        for (int i = 1; i <= n; i++) {
            dq.offer(i);
        }
        sb.append("<");
        while (dq.size() != 1) {
            for (int i = 0; i < k-1; i++) {
                dq.offer(dq.poll());
            }
            sb.append(dq.poll()).append(", ");
        }
        sb.append(dq.poll() + ">");
        System.out.println(sb);
    }
}