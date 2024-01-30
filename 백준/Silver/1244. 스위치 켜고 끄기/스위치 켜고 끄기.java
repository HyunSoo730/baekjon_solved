import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * @author 조현수
 * @date 23.1.30
 * @link https://www.acmicpc.net/problem/1244
 * @keyword_solution
 * @input
 * @output
 * @time_complex
 * @perf 메모리 ~, 소요시간 ~
 */
public class Main {

    /**
     * 남자 : 스위치 번호가 자기가 받은 수의 배수 -> 상태 바꿈 (꺼짐 -> 켜짐 이런 식으로)
     * 여자 : 본인이 받은 수와 같은 번호가 붙은 스위치를 중심으로
     * 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간 찾은 후 그 구간에 속한 스위치 상태 모두 바꿈
     */
    static int n, m;  //스위치 개수, 학생 수
    static int[] data;
    static int[] p;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        data = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        m = Integer.parseInt(br.readLine());
        p = new int[m];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            switchData(gender, num);
        }
        for (int i = 1; i <= n; i++) {
            System.out.print(data[i] + " ");
            if (i % 20 == 0) {
                System.out.println();
            }
        }
    }

    public static void switchData(int gen, int num) {
        if (gen == 1) { // 남자인 경우
            for (int i = 0; i <= n; i += num) {
                if(num + i > n) break;
                data[num + i] = data[num + i] == 0 ? 1 : 0;
            }
        }else{  // 여자
            // 현재 좌표 num 기준 양 사이드 확인 .
            for (int i = 1; i <= n; i++) {
                if (num - i < 1 || num + i > n) {
                    break;
                }
//                System.out.println(data[num-i] == data[num+i]);
//                System.out.println("num-i = " + (num - i) + " num+i = " + (num+i));
                if (data[num - i] == data[num + i]) {
                    data[num + i] = data[num + i] == 0 ? 1 : 0;
                    data[num - i] = data[num - i] == 0 ? 1 : 0;
                } else {
                    break;
                }
            }
            data[num] = data[num] == 0 ? 1 : 0;
        }
    }
}