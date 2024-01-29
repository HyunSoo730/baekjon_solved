import java.io.*;
import java.util.*;

public class Main {

	static int[][] data = new int[20][20];
	static int cntA = 0; // 검은돌
	static int cntB = 0; // 흰 돌
	static boolean checkA = false; // 검은돌 연속성 확인
	static boolean checkB = false; // 흰돌 연속성 확인
	static int startX, startY;
	static int winColor;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("Test5.txt"));
		// 여기에 코드를 작성하세요.
		Scanner sc = new Scanner(System.in);

		for (int i = 1; i <= 19; i++) {
			for (int j = 1; j <= 19; j++) {
				data[i][j] = sc.nextInt();
			}
		}

		boolean flag = false;
		outer: for (int i = 1; i <= 19; i++) {
			for (int j = 1; j <= 19; j++) {
				// 현재 좌표에서 검사 진행
				if (isFinishCol(i, j, 1)) { // 검은돌 이긴 경우
					flag = true;
					winColor = 1;
					startX = i;
					startY = j;
					break outer;
				}
				if (isFinishCol(i, j, 2)) {
					flag = true;
					winColor = 2;
					startX = i;
					startY = j;
					break outer;
				}
				if (isFinishRow(i, j, 1)) {
					flag = true;
					winColor = 1;
					startX = i;
					startY = j;
					break outer;
				}
				if (isFinishRow(i, j, 2)) {
					flag = true;
					winColor = 2;
					startX = i;
					startY = j;
					break outer;
				}
				if (isFinishD1(i, j, 1)) {
					flag = true;
					winColor = 1;
					startX = i;
					startY = j;
					break outer;
				}
				if(isFinishD1(i, j, 2)) {
					flag = true;
					winColor = 2;
					startX = i;
					startY = j;
					break outer;
				}
				if(isFinishD2(i, j, 1)) {
					flag = true;
					winColor = 1;
					startX = i;
					startY = j;
					break outer;
				}
				if (isFinishD2(i, j, 2)) {
					flag = true;
					winColor = 2;
					startX = i;
					startY = j;
					break outer;
				}
			}
		}

		if (flag) {
			System.out.println(winColor);
			System.out.println(startX + " " + startY);
		}else {
			System.out.println(0);
		}

	}

	public static boolean isInner(int i, int j) {
		if (i < 1 || i > 19 || j < 1 || j > 19) {
			return false;
		}
		return true;
	}

	public static boolean isFinishCol(int x, int y, int color) {
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (isInner(x, y + i) && data[x][y + i] == color) {
				cnt += 1;
			}
		}
		if(cnt != 5) return false;
		if (cnt == 5) {
			// 여기서 이제 유효성 검사 진행
			if (isInner(x, y - 1) && (data[x][y - 1] == color)) {
				return false;
			}
			if (isInner(x, y +5) && data[x][y +5] == color) {
				return false;
			}
		}
		return true;
	}

	public static boolean isFinishRow(int x, int y, int color) {
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (isInner(x + i, y) && data[x + i][y] == color) {
				cnt += 1;
			}
		}
		if(cnt != 5) return false;
		if (cnt == 5) { // 시작점 -1, 끝점 + 1 기준으로 검사해야함
			if (isInner(x - 1, y) && data[x - 1][y] == color) {
				return false;
			}
			if (isInner(x +5, y) && data[x +5][y] == color) {
				return false;
			}
		}
		return true;
	}

	public static boolean isFinishD1(int x, int y, int color) {
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (isInner(x + i, y + i) && data[x + i][y + i] == color) {
				cnt += 1;
			}
		}
		if(cnt != 5) return false;
		if (cnt == 5) { // 시작점 -1, 끝점 + 1 기준으로 검사해야함
			if (isInner(x - 1, y - 1) && data[x - 1][y - 1] == color) {
				return false;
			}
			if (isInner(x + 5, y + 5) && data[x + 5][y + 5] == color) {
				return false;
			}
		}
		return true;
	}

	public static boolean isFinishD2(int x, int y, int color) {
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (isInner(x - i, y + i) && data[x - i][y + i] == color) {
				cnt += 1;
			}
		}
		if(cnt != 5) return false;
		if (cnt == 5) { // 시작점 -1, 끝점 + 1 기준으로 검사해야함
			if (isInner(x + 1, y - 1) && data[x + 1][y - 1] == color) {
				return false;
			}
			if (isInner(x - 5, y + 5) && data[x - 5][y + 5] == color) {
				return false;
			}
		}
		return true;
	}

}