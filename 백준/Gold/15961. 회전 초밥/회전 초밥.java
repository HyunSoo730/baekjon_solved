import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, d, k, c; // ! 접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수, 쿠폰 번호
    static int[] data;
    static int res;
    static Map<Integer, Integer> map = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < k - 1; i++) {
            map.put(data[i%n], map.getOrDefault(data[i%n], 0) + 1);
        }
        int start = 0;
        int max = 0;
        for (int end = k - 1; end < n + k -1; end++) {
            // 먼저 끝점부터 넣어주기
            map.put(data[end%n], map.getOrDefault(data[end%n], 0) + 1);
            if (!map.keySet().contains(c)) {
                max = Math.max(max, map.size() + 1);
            } else {
                max = Math.max(max, map.size());
            }
            // 시작점 빼기
            map.put(data[start%n], map.get(data[start%n]) -1);
            if (map.get(data[start%n]) == 0) {
                map.remove(data[start%n]);  // 해당 윈도우 제거
            }
            start += 1;
        }

        System.out.println(max);
    }
}