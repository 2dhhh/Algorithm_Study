package fastcampus.brute_force;

import java.io.*;

public class no11068 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //테스트 케이스 입력
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            for (int j = 2; j <= 64; j++) {
                int num = n;
                int count = divideCount(n, j);
                int[] arr = new int[count+1];
                for (int k = 0; k < count + 1; k++) {
                    arr[k] = num % j;
                    num /= j;
                }
                if(isPelindrom(arr)){
                    bw.write("1\n");
                    break;
                }
                if (j == 64) {
                    bw.write("0\n");
                }
            }
        }
        bw.flush();
        bw.close();
    }
    static int divideCount(int n, int j) {
        int count = 0;
        while (n / j > 0) {
            count++;
            n /= j;
        }
        return count;
    }

    static boolean isPelindrom(int[] arr) {
        for(int i = 0; i < arr.length/2; i++){
            if (arr[i] != arr[arr.length - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}
