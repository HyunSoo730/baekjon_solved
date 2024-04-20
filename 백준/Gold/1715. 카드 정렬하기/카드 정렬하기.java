import java.io.*;
import java.util.*;



public class Main {

    static int n;
    static int[] data;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            pq.offer(num);
        }

        int res = 0;
        while (pq.size() > 1) {
            int numA = pq.poll();
            int numB = pq.poll();
            res += numA + numB;
            pq.offer(numA + numB);
        }

        System.out.println(res);

    }
}