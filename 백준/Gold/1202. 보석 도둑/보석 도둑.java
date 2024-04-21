import java.io.*;
import java.util.*;



public class Main {

    // ! 보석 도둑
    static int n, k;
    static long weight, value; // ! 보석의 무게, 가치
    static List<Long> bags = new ArrayList<>();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    private static class Data implements Comparable<Data>{
        long weight, value;

        Data(long weight, long value) {
            this.weight = weight;
            this.value = value;
        }

        @Override
        public int compareTo(Data data) {
            if (this.weight == data.weight) {
                Long.compare(data.value, this.value);
            }
            return Long.compare(this.weight, data.weight); // ! 무게 기준 오름차순 먼저 2. 같다면 가치 기준 내림차순 진행
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); // ! n개의 보석
        k = Integer.parseInt(st.nextToken()); // ! k개의 가방
        PriorityQueue<Data> pq = new PriorityQueue<>();
        PriorityQueue<Long> temp = new PriorityQueue<>((a,b) -> b.compareTo(a));
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            weight = Long.parseLong(st.nextToken());
            value = Long.parseLong(st.nextToken());
            pq.offer(new Data(weight, value));
        }
        for (int i = 0; i < k; i++) {
            long max_weight = Long.parseLong(br.readLine());
            bags.add(max_weight);
        }

        Collections.sort(bags); // ! 오름차순 정렬
        long res = 0;
        for (int i = 0; i < k; i++) {
            long max_weight = bags.get(i); // ! 가방의 최대 무게 가져온 후
            while (!pq.isEmpty() && pq.peek().weight <= max_weight) {
                Data data = pq.poll();
                temp.offer(data.value); // ! 후보군 등록
            }

            if (!temp.isEmpty()) { // ! 존재하면 더해야함
                res += temp.poll();
            }
        }
        System.out.println(res);
    }
}