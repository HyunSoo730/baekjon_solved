import java.io.*;
import java.util.*;



public class Main {

    // ! 수 묶기
    static int n;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> plus = new PriorityQueue<>((a, b) -> b.compareTo(a)); // ! 양수는 내림차순
        PriorityQueue<Integer> minus = new PriorityQueue<>(); // ! 음수는 오름차순
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if(num > 0) plus.offer(num);
            else minus.offer(num);
        }

        List<Integer> temp = new ArrayList<>();
        int res = 0;
        while (plus.size() > 1) {
            int numA = plus.poll();
            int numB = plus.poll();
            if (numA * numB > numA + numB) {
                res += numA * numB;
            }else{
                res += numA + numB;
            }
        }

        if (!plus.isEmpty()) {
            temp.add(plus.poll());
        }

        while (minus.size() > 1) {
            int numA = minus.poll();
            int numB = minus.poll();
            if (numA * numB > numA + numB) {
                res += numA * numB;
            }else{
                res += numA + numB;
            }
        }

        if (!minus.isEmpty()) {
            temp.add(minus.poll());
        }

        if (temp.size() == 2) {
            int numA = temp.get(0);
            int numB = temp.get(1);
            if(numA * numB > numA + numB){
                res += numA * numB;
            }else{
                res += numA + numB;
            }
        } else if (temp.size() == 1) {
            res += temp.get(0);
        }

        System.out.println(res);

    }
}