import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    static int n, m;
    static Map<Character, Integer> map = new HashMap<>();
    static Map<Character, Integer> now = new HashMap<>();
    static char[] arr = {'A', 'C', 'G', 'T'};
    static Map<Character, Integer> checkCount = new HashMap<>();
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());  // 총 문자열 길이
        m = Integer.parseInt(st.nextToken());  // 원하는 부분 문자열 길이
        String data = br.readLine();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            checkCount.put(arr[i], Integer.parseInt(st.nextToken()));
        }

        // 부분 문자열 생성.
        for (int i = 0; i < m; i++) {
            map.put(data.charAt(i), map.getOrDefault(data.charAt(i), 0) + 1);
        }
        if (isCheck()) {
            count += 1;
        }
        for (int i = 0; i < n - m; i++) {
            char s = data.charAt(i);
            char e = data.charAt(i + m);
            map.put(s, map.get(s) - 1);  // 앞에꺼 제거
            if(map.get(s) == 0) map.remove(s);
            map.put(e, map.getOrDefault(e, 0) + 1);  // 마지막 꺼 추가
            if (isCheck()) {
                count += 1;
            }
        }
        System.out.println(count);

    }

    public static boolean isCheck() {
        for (char c : arr) {
            if (map.getOrDefault(c, 0) < checkCount.get(c)) {
                return false;
            }
        }
        return true;
    }
}