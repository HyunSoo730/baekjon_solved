import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Solution {

    static int T;
    static int n;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int t = 1; t <= 10; t++) {
            n = Integer.parseInt(br.readLine());
            int ans = 1;
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                st.nextToken();  // 정점 번호는 패스
                char val = st.nextToken().charAt(0);
                if (st.hasMoreTokens()) {  // 리프노드 아님
                    if (val >= '0' && val <= '9') {
                        ans = 0;
                    }
                } else {  // 뒤에 값 X -> 리프 노드
                    if (val < '0' || val > '9') {
                        ans = 0;
                    }
                }
            }
            System.out.println("#" + t + " " + ans);
        }
    }

}