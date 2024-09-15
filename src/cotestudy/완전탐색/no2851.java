package cotestudy.완전탐색;

import java.io.*;

public class no2851 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int sum = 0;
        int ans = Integer.MAX_VALUE;
        int[] intArray = new int[10];
        for (int i = 0; i < 10; i++) {
            intArray[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < 10; i++) {
            sum += intArray[i];
            if(sum == 100){
                ans = 100;
                break;
            }
            if (Math.abs(sum - 100) <= Math.abs(ans-100)) {
                ans = sum;
            }
        }
        bw.write(ans + "");
        bw.flush();
        bw.close();
    }
}
