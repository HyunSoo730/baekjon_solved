import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, ans = -1;
	static boolean[] selected = new boolean[10];
	static int[] players = new int[10];
	static int[][] arr;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		arr = new int[N][10];
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=1;j<=9;j++) {
				arr[i][j]= Integer.parseInt(st.nextToken());
			}
		}
		
		// 1번 선수는 4번 타자로 미리 결정 
		players[4] = 1;
		selected[4]=true;
		
		permutation(2);
		System.out.println(ans);

	}
	
	// 타순 정하기
	private static void permutation(int cnt) {
		
		if(cnt==10) {
			// 순서가 정해지면 게임 시작
			ans = Math.max(ans, game());
			return;
		}
		
		for(int i=1;i<=9;i++) {
			if(!selected[i]) {
				selected[i] = true;
				players[i] = cnt;
				permutation(cnt+1);
				selected[i] = false;
			}
		}
	}
	
	// 게임 진행
	private static int game() {
		int start = 1;
		int score = 0;
		
		for(int i=0;i<N;i++) {
			
			// 각 주자들의 위치를 저장하기 위한 배열( 아웃은 0번 인덱스에 저장 )
			int[] point = {0,0,0,0,0};
			
			// 아웃이 3번이 되기 전까지 진행
			while(point[0]<3) {
				run(point,arr[i][players[start]]);
				if(start==9) {
					start=1;
				}else {
					start++;
				}
			}
			
			// 한 이닝이 끝나면 얻은 점수를 score에 저장
			score += point[4];
		}
		return score;
	}
	
	// 모든 주자들 이동
	private static void run(int[] point, int n) {
		
		for(int i=0;i<n;i++) {
			// 홈으로 들어온 주자들의 수는 point[4]에 축적됨 = 점수
			point[4]+=point[3];
			point[3]=point[2];
			point[2]=point[1];
			point[1]=0;
		}
		
		// 이전에 나가있던 주자들을 이동시킨 후에 새로 공을 친 주자의 위치를 저장
		point[n]++;
	}
	


}