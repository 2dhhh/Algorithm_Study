package brute_force;

import java.io.*;

public class no1730 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //n의 크기 입력
        int n = Integer.parseInt(br.readLine());
        //조각도 입력
        String str = br.readLine();
        //격자 배열 선언 및 점 입력
        char[][] charArray = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                charArray[i][j] = 46;
            }
        }
        //현재 위치 선언
        int x = 0;
        int y = 0;
        //조각도에 따라 움직임 로직
        for (int i = 0; i < str.length(); i++) {
            int dx = x;
            int dy = y;

            if (str.charAt(i) == 'U') {
                dy--;
            }else if(str.charAt(i) == 'D'){
                dy++;
            } else if(str.charAt(i) == 'R') {
                dx++;
            } else if (str.charAt(i) == 'L') {
                dx--;
            }

            //격자판에서 벗어나면 다음단계로 이동
            if (dx < 0 || dx >= n || dy < 0 || dy >= n) {
                continue;
            }
            //현재위치 움직임 표시
            if(charArray[y][x] == 46 && (str.charAt(i) == 'L'|| str.charAt(i) == 'R')){
                charArray[y][x] = 45;
            } else if (charArray[y][x] == 46 && (str.charAt(i) == 'U' || str.charAt(i) == 'D')) {
                charArray[y][x] = 124;
            } else if ((charArray[y][x] == 45 && (str.charAt(i) == 'U' || str.charAt(i) == 'D'))
                    || (charArray[y][x] == 124 && (str.charAt(i) == 'L' || str.charAt(i) == 'R'))) {
                charArray[y][x] = 43;
            }

            //이동한 위치(dx,dy)에 대한 움직임 표시
            if(charArray[dy][dx] == 46 && (str.charAt(i) == 'U' || str.charAt(i) == 'D')){
                charArray[dy][dx] = 124;
            } else if (charArray[dy][dx] == 46 && (str.charAt(i) == 'L' || str.charAt(i) == 'R')) {
                charArray[dy][dx] = 45;
            } else if ((charArray[dy][dx] == 45 && (str.charAt(i) == 'U' || str.charAt(i) == 'D'))
                    || (charArray[dy][dx] == 124 && (str.charAt(i) == 'L' || str.charAt(i) == 'R'))) {
                charArray[dy][dx] = 43;
            }


            //현재 위치 업데이트
            x = dx;
            y = dy;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                bw.write(charArray[i][j]);
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
