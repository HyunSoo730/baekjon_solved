import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    // ! 과일 하나 먹으면 길이 + 1, 과일은 일정 높이를 가짐
    // ! 자신의 길이 >= 과일 높이 인 과일들만 먹음
    // ! 처음 길이 L, 과일 먹어서 늘릴 수 있는 최대 길이

    static int n, L;
    static int[] data;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        data = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(data);
        for (int i = 0; i < n; i++) {
            if(L >= data[i]) L+=1;
        }
        System.out.println(L);
    }
}