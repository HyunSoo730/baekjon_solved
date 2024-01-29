import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    //원래 메모리가 무슨 값이었는지 알고 있음.
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int T;
    static int[] data;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            String memory = br.readLine();
            data = new int[memory.length()];
            for (int i = 0; i < data.length; i++) {
                data[i] = Character.getNumericValue(memory.charAt(i));
            }
            // 해당 숫자 확인해서 카운팅
            int cnt = data[0];  // 시작지점이 1이면 카운트하고 시작
            int last = data[0];
            for (int i = 0; i < data.length; i++) {
                if (last != data[i]) {
                    cnt += 1;
                    last = data[i];
                }
            }
            System.out.println("#" + t + " " + cnt);
        }
    }
}