package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no2309 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] intArray = new int[9];
        int sum = 0;
        int ans1 = 0;
        int ans2 = 0;
        for (int i = 0; i < 9; i++) {
            intArray[i] = Integer.parseInt(br.readLine());
            sum += intArray[i];
        }
        Arrays.sort(intArray);
        int ans = sum - 100;
        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (intArray[i] + intArray[j] == ans) {
                    ans1 = intArray[i];
                    ans2 = intArray[j];
                    break;
                }
            }
        }
        for (int i = 0; i < 9; i++) {
            if (intArray[i] != ans1 && intArray[i] != ans2) {
                bw.write(intArray[i] + "\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
