import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

class Solution
{

    public static void main(String args[]) throws Exception
    {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T;
        T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++)
        {
            br.readLine();
            st = new StringTokenizer(br.readLine());
            int[] data = new int[1000];
            for (int i = 0; i < 1000; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }
            int[] cnt = new int[101];
            for (int i = 0; i < 1000; i++) {
                cnt[data[i]] += 1;
            }

            int max = 0;
            int idx = 0;
            for (int i = 0; i < cnt.length; i++) {
                if (cnt[i] >= max) {
                    max= cnt[i];
                    idx = i;
                }
            }

            System.out.println("#" + test_case + " " + idx);
        }
    }


}