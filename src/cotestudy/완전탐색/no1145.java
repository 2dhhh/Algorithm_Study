package cotestudy.완전탐색;
import java.io.*;
import java.util.*;

public class no1145 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] intArray = new int[5];
        for (int i = 0; i < 5; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }
        int ans = 0;
        for (int i = 1; i < 1_000_000; i++) {
            int cnt = 0;
            for (int j = 0; j < 5; j++) {
                if (i % intArray[j] == 0) {
                    cnt++;
                }
            }
            if (cnt >= 3) {
                ans = i;
                break;
            }
        }
        bw.write(ans + "");
        bw.flush();
        bw.close();
    }
}
