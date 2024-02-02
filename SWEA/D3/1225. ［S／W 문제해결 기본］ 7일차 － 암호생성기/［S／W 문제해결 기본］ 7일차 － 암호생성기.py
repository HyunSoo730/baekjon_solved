import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {

    /**
     * ! 8자리 암호 생성 , 8개 숫자 입력 받음.
     * * 덱을 이용해서 해결
     */

    static int t, T = 10;
    static int[] data;
    static Deque<Integer> dq;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int tc = 1; tc <= T; tc++) {
            t = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            dq = new ArrayDeque<>();
            for (int i = 0; i < 8; i++) {
                dq.offer(Integer.parseInt(st.nextToken()));
            }

            outer :
            while (true) {
                for (int i = 1; i <= 5; i++) {
                    int num = dq.poll();
                    if (num - i <= 0) {
                        dq.offer(0);
                        break outer;
                    } else {
                        dq.offer(num - i);
                    }
                }
            }
            sb.append("#").append(tc).append(" ");
            for (int i = 0; i < 8; i++) {
                sb.append(dq.poll()).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}