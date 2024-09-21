package cotestudy.완전탐색;
import java.io.*;
import java.util.*;

public class no2563 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[][] intArray = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            intArray[i][0] = Integer.parseInt(st.nextToken());
            intArray[i][1] = Integer.parseInt(st.nextToken());
        }
        int count = 0;
        boolean[][] booleanArray = new boolean[101][101];
        for (int i = 0; i < n; i++) {
            int x = intArray[i][0];
            int y = intArray[i][1];
            for (int k = x ; k < x + 10; k++) {
                for (int l = y; l < y + 10; l++) {
                    if (!booleanArray[k][l]) {
                        booleanArray[k][l] = true;
                        count++;
                    }
                }
            }
        }
        bw.write(count + "");
        bw.flush();
        bw.close();
    }
}
