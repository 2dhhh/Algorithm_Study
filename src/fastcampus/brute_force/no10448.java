package fastcampus.brute_force;
import java.io.*;
public class no10448 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //삼각수 해당하는 배열 선언
        int[] tArray = new int[46];
        for (int i = 1; i < 46; i++) {
            tArray[i] = (i * (i + 1)) / 2;
        }
        int testNum = Integer.parseInt(br.readLine());
        int checkNum;

        for (int i = 0; i < testNum; i++) {
            // 로직이 들어갈 부분
            // 자연수 입력 받기
            int naturalNum = Integer.parseInt(br.readLine());
            int maxIdx = 0;
            for (int j = 1; j < 46; j++) {
                if(naturalNum <= tArray[j]) {
                    maxIdx = j;
                    break;
                }
            }
            checkNum = 0;

            for (int j = 1; j < maxIdx; j++) {
                for (int k = 1; k < maxIdx; k++) {
                    for (int l = 1; l < maxIdx; l++) {
                        if(tArray[j] + tArray[k] + tArray[l] == naturalNum) {
                            checkNum++;
                            break;
                        }
                    }
                    if (checkNum != 0) {
                        break;
                    }
                }
                if (checkNum != 0) {
                    break;
                }
            }
            if (checkNum != 0) {
                bw.write(1 + "\n");
            } else bw.write(0 + "\n");
        }
        bw.flush();
        bw.close();
    }
}
