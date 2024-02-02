import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {


    static int n;
    static Deque<Integer> dq = new ArrayDeque<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        for (int i = 1; i <= n; i++) {
            dq.offer(i);
        }
        while (dq.size() > 1) {
            dq.poll();  // 첫번째 숫자 버리기
            dq.offer(dq.poll());
        }
        System.out.println(dq.poll());
    }
}