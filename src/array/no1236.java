package array;

import java.io.*;
import java.util.StringTokenizer;

public class no1236 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        //세로 크기
        int n = Integer.parseInt(st.nextToken());
        //가로 크기
        int m = Integer.parseInt(st.nextToken());

        int row = 0;
        int col = 0;

        String[] str = new String[n];
        // 배열에 대한 입력 및 행에 경비원 존재여부 파악
        for (int i = 0; i < n; i++) {
            str[i] = br.readLine();
            if (!str[i].contains("X")) {
                row++;
            }
        }

        // 세로를 기준으로 카운트
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (str[j].charAt(i) == 'X') {
                    break;
                }
                if(j == n-1){
                    col++;
                }
            }
        }
        if (row >= col) {
            bw.write(String.valueOf(row));
        }
        else {
            bw.write(String.valueOf(col));
        }
        bw.flush();
        bw.close();

    }
}
