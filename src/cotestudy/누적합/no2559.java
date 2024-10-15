package cotestudy.누적합;

import java.io.*;
import java.util.*;
public class no2559 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] intArray = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }

        int sum;
        int max = Integer.MIN_VALUE;
//        누적 합
        int[] prefix_sum = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            prefix_sum[i] = prefix_sum[i - 1] + intArray[i - 1];
        }
        for (int i = k; i <= n; i++) {
            sum = prefix_sum[i] - prefix_sum[i-k];
            if (sum > max) {
                max = sum;
            }
        }
//         완전탐색
//        for (int i = 0; i < n - k + 1; i++) {
//            sum = intArray[i];
//            for (int j = i + 1; j < i + k; j++) {
//                sum += intArray[j];
//            }
//            if (sum > max) {
//                max = sum;
//            }
//        }
        bw.write(max + "");
        bw.flush();
        bw.close();
    }

}
