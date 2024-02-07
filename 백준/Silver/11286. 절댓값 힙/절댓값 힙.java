import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class Main {

    private static class Data implements Comparable<Data>{
        int rawData;
        int absData;

        Data(int data) {
            this.rawData = data;
            this.absData = Math.abs(data);
        }

        @Override
        public int compareTo(Data o) {
            if(this.absData == o.absData) return this.rawData - o.rawData;
            else return absData - o.absData;
        }
    }
    static int n;
    static PriorityQueue<Data> pq = new PriorityQueue<Data>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        int x;
        for (int i = 0; i < n; i++) {
            x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if(pq.isEmpty()) System.out.println(0);
                else System.out.println(pq.poll().rawData);
            } else {
                pq.offer(new Data(x));
            }
        }
    }
}