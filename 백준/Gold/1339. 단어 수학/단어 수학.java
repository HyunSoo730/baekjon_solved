import java.io.*;
import java.util.*;



public class Main {

    static int n;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static List<String> data = new ArrayList<>();
    static Map<Character, Integer> map = new HashMap();
    static Map<Character, Integer> num_map = new HashMap<>();

    static String[] words;
    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());
        words = new String[n];
        for (int i = 0; i < n; i++) {
            String data = br.readLine();
            words[i] = data;
            for (int j = 0; j < data.length(); j++) {
                char c = data.charAt(j); // ! 변환
//                System.out.println(Math.pow(10, data.length() - j - 1));
                map.put(c, map.getOrDefault(c, 0) + (int) Math.pow(10, data.length() - j - 1));
            }
        }
//        System.out.println("끝나고확인 : " + map);
        // ! 알파벳의 가치를 기준으로 내림차순 정렬
        // ! List로 정렬 후 사용
//        List<Character> chars = new ArrayList<>(map.keySet());
//        Collections.sort(chars, (a, b) -> map.get(b) - map.get(a));
        // ! Collections.sort를 통해 List형태로 Map 가져오기
        List<Map.Entry<Character, Integer>> entryList = new ArrayList<>(map.entrySet());
        // ! 이 entrySet을 정렬하는 방법 사용
        // ! entry의 값을 기준으로 내림차순 정렬 진행.
        Collections.sort(entryList, (a, b) -> b.getValue() - a.getValue());
        // ! 알파벳에 숫자 할당
        int num = 9;
//        for (char c : chars) {
//            num_map.put(c, num);
//            num -= 1;
//        }
        for (Map.Entry<Character, Integer> entry : entryList) {
            num_map.put(entry.getKey(), num);
            num -= 1;
        }
        // ! 정렬된 entryList를 순회하면서 각 엔트리의 키를 사용하여 num_map에 알파벳 숫자를 매핑
//        System.out.println(num_map);
        // ! 최종 결과
        int res = 0;
        for (String word : words) {
            int value = 0;
            for (char c : word.toCharArray()) {
                value = value * 10 + num_map.get(c);
            }
            res += value;
        }
//        System.out.println(map);
//        System.out.println(num_map);
        System.out.println(res);
    }
}