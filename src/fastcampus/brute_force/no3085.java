package fastcampus.brute_force;

import java.io.*;
public class no3085 {
    public static int n;
    public static char[][] charArray;
    public static int max = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //N의 크기 입력
        n = Integer.parseInt(br.readLine());
        charArray = new char[n][n];

        //N * N 입력
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                charArray[i][j] = str.charAt(j);
            }
        }

        //행 인접한 다른 문자 변경
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n-1; j++) {
                if (charArray[i][j] != charArray[i][j+1]) {
                    char tmp = charArray[i][j];
                    charArray[i][j] = charArray[i][j+1];
                    charArray[i][j+1] = tmp;

                    checkArray();

                    //원래대로 복구
                    tmp = charArray[i][j];
                    charArray[i][j] = charArray[i][j+1];
                    charArray[i][j+1] = tmp;
                }
            }
        }
        //열 인접한 다른 문자 변경
        for(int i = 0; i < n; i++) {
            for (int j = 0; j < n -1; j++) {
                if(charArray[j][i] != charArray[j+1][i]){
                    char tmp = charArray[j][i];
                    charArray[j][i] = charArray[j+1][i];
                    charArray[j+1][i] = tmp;

                    checkArray();

                    tmp = charArray[j][i];
                    charArray[j][i] = charArray[j+1][i];
                    charArray[j+1][i] = tmp;
                }
            }
        }

        bw.write(String.valueOf(max));
        bw.flush();
        bw.close();
    }

    public static void checkArray(){


        //행 체크
        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = 0; j < n-1; j++) {
                //이전 문자와 동일한 경우
                if (charArray[i][j] == charArray[i][j + 1]) {
                    count++;
                }
                //이전 문자와 동일하지 않은 경우
                else {
                    count = 1;
                }
                max = Math.max(max, count);
            }
        }
        //열 체크
        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = 0; j < n - 1; j++) {
                if (charArray[j][i] == charArray[j+1][i]) {
                    count++;
                }
                else {
                    count = 1;
                }
                max = Math.max(max, count);
            }
        }
    }
}
