package cotestudy.투포인터;
import java.io.*;
import java.util.Arrays;

public class no2309 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] intArray = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            intArray[i] = Integer.parseInt(br.readLine());
            sum += intArray[i];
        }
        Arrays.sort(intArray);

        int s = 0, e = 8, ans = sum-100;
        while (s <= e) {
            if (intArray[s] + intArray[e] == ans) {
                break;
            }

            else if (intArray[s] + intArray[e] > ans) {
                e--;
            }
            else s++;
        }

        for (int i = 0; i < 9; i++) {
            if (i == s || i == e) {
                continue;
            }
            bw.write(intArray[i] + "\n");
        }
        bw.flush();
        bw.close();
    }
}
