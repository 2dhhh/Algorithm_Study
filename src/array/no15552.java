package array;

import java.io.*;
import java.util.StringTokenizer;

public class no15552 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        // 테스트 케이스 개수 T
        int t = Integer.parseInt(br.readLine());
        int a;
        int b;
        int sum;

        for (int i = 0; i < t; i++) {
            String s = br.readLine();
            st = new StringTokenizer(s);
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            sum = a + b;
            bw.write(sum + "\n");

        }
        bw.flush();
        bw.close();


    }
}
