package fastcampus.stirng;
import java.io.*;


public class no1157 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int maxIndex = 0;
        int count = 0;
        //입력 및 데이터 대문자로 전처리
        String str = br.readLine().toUpperCase();

        //알파벳 개수 저장 배열 선언
        int[] intArray = new int[26];

        //문자열 알파벳 배열에 저장
        for (int i = 0; i < str.length(); i++) {
            intArray[str.charAt(i) - 'A']++;
        }

        //가장 큰 값을 갖는 배열 값 찾기
        for (int i = 1; i < 26; i++) {
            if (intArray[maxIndex] < intArray[i]) {
                count = 0;
                maxIndex = i;
            }
            else if (intArray[maxIndex] == intArray[i]) {
                count++;
            }
        }

        if (count > 0) {
            bw.write("?");
        }
        else {
            char ch = (char) (maxIndex + 'A');
            bw.write(ch);
        }
        bw.flush();
        bw.close();
    }
}

