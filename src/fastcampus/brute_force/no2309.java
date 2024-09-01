package fastcampus.brute_force;
import java.io.*;

public class no2309 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //난쟁이 집어넣을 배열 선언
        int[] intArr = new int[9];
        for (int i = 0; i < 9; i++) {
            intArr[i] = Integer.parseInt(br.readLine());
        }

        //아홉명의 난장이 키의 합
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            sum += intArr[i];
        }

        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (sum - intArr[i] - intArr[j] == 100) {
                    intArr[i] = 0;
                    intArr[j] = 0;
                    break;
                }
            }
            if (intArr[i] == 0) {
                break;
            }
        }

        //오름차순 정렬을 위한 배열 선언
        int[] intArr2 = new int[100];
        for (int i = 0; i < 9; i++) {
            if (intArr[i] != 0) {
                intArr2[intArr[i]]++;
            }
        }
        for (int i = 0; i< intArr2.length; i++) {
            if (intArr2[i] != 0) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
