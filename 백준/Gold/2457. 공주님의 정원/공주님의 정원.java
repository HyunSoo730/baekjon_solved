import org.w3c.dom.Node;

import java.awt.*;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;

    private static class Data implements Comparable<Data>{
        int start, end;

        Data(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Data data) {
            if(this.start == data.start) return data.end - this.end;
            else return this.start - data.start;
        }
    }

    // ! 1. 시작점 오름차순 2. 끝점 내림차순
    static List<Data> list = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int startMonth = Integer.parseInt(st.nextToken());
            int startDay = Integer.parseInt(st.nextToken());
            int endMonth = Integer.parseInt(st.nextToken());
            int endDay = Integer.parseInt(st.nextToken());
            int start = 100 * startMonth + startDay;
            int end = 100 * endMonth + endDay;

            list.add(new Data(start, end));
        }

        Collections.sort(list);

        // ! 현재 선택한 꽃의 종료 날짜를 기준으로 다음에 올 꽃을 선택.
        // ! 현재 꽃의 종료 날짜보다 시작 날짜가 작거나 같고, 종료날짜가 가장 큰 꽃을 선택. -> 이렇게 함으로써 항상 최대 기간을 커버
        // ! 선택한 종료 날짜를 갱신하고 이 과정 반복 (만약 어떤 시점에서 추가적으로 꽃 선택 X -> 안되는거임)

        int lastEnd = 301;  // ! 3월1일부터 시작
        int endDay = 1201;
        int maxEnd =0;  // 최대한의 종료일
        int index = 0;
        int cnt = 0;

        // * 꽃이 지는 기간(end)가 12월1일 이상인 꽃을 최후로 받으면 된다.
        // * 가장 오래 피어있는 꽃을 어떻게 찾을지 고민하는 것이 중요했음.
        while (lastEnd < endDay) { // ! 마지막으로 선택한 꽃의 end가 12월1일보다 적은 경우만.
            boolean isFind = false;
            for (int i = index; i < list.size(); i++) {
                Data now = list.get(i);  // ! 현재 꽃
                if (now.start > lastEnd) {
                    break;
                }

                if (now.end < 301) {
                    continue;  // 3월1일 전에 피고지는 꽃은 제외
                }

                if (now.end > maxEnd) {
                    maxEnd = now.end;
                    isFind = true;
                    index = i+1;  // ! 그 다음부터 돌아야 할 꽃
                    // ! -> 현재 반복에서 선택된 꽃이 가장 늦게 지는 꽃. 이 꽃의 종료 날짜(maxEnd)를 기준으로
                    //! 다음 꽃을 선택할 때, 이미 고려된 꽃들을 건너뛰고 다음 꽃부터 검사하려는 의도. 
                }
            }

            if (isFind) {
                cnt += 1;
                lastEnd = maxEnd;  // ! 다시 갱신.
            } else {
                break;
            }
        }

        if (lastEnd < endDay) {
            System.out.println(0);
        } else {
            System.out.println(cnt);
        }
    }



}