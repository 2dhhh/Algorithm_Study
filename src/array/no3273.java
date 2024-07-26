package array;

import java.io.*;
import java.util.StringTokenizer;

public class no3273 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //수열의 크기
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        //카운팅 배열 선언 및 배열 입력
        int[] cntArr = new int[2000001];
        for(int i = 0 ; i < n ; i++){
            cntArr[Integer.parseInt(st.nextToken())]++;
        }
        //x값 입력
        int x = Integer.parseInt(br.readLine());
        int count = 0;


        for (int i = 1; i < x; i++) {
            if (cntArr[i] == 1 && cntArr[x - i] == 1) {
                count++;
            }
        }
        count /= 2;
        bw.write(String.valueOf(count));
        bw.flush();
        bw.close();
    }
}
