import java.io.*;
import java.util.*;



public class Main {

    static int n;
    private static class Data implements Comparable<Data>{
        int start, end;

        Data(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Data data) {
            if (this.start == data.start) {
                return this.end - data.end;
            }
            return this.start - data.start;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        List<Data> data = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            data.add(new Data(start, end));
        }
        Collections.sort(data); // ! 시작시간 오름차순, 그 후 끝나는 시간 오름차순
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> a.compareTo(b)); // ! 오름차순 정렬 -> 끝나는 시간만

        for (Data d : data) {
            int start = d.start;
            int end = d.end;
            if (!pq.isEmpty() && pq.peek() <= start) { // ! 큐 안 비어있으면서, 현재 강의의 시작시간이 우선순위 큐에 들어있는 가장 빨리 끝나는 시간보다 같거나 크면 이어서 가능
                pq.poll(); // ! 마지막 꺼 버려
            }
            pq.offer(end); // ! 마지막 시간은 언제나 갱신.
        }

        int res = pq.size();
        System.out.println(res);
    }
}