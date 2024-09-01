package fastcampus.stirng;

import java.io.*;

public class no1919 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //알파벳 저장할 배열 선언
        int[] intArray = new int[26];

        //최소로 지워야하는 개수 변수 선언
        int count = 0;

        //입력 값
        String str1 = br.readLine();
        String str2 = br.readLine();

        //입력 값 배열에 저장
        for (int i = 0; i < str1.length(); i++) {
            intArray[str1.charAt(i) - 'a']++;
        }

        //동일한 문자가 존재하느지 확인
        for (int i = 0; i < str2.length(); i++) {
            intArray[str2.charAt(i) - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            count += Math.abs(intArray[i]);
        }
        bw.write(String.valueOf(count));
        bw.flush();
        bw.close();
    }
}
