package stirng;

import java.io.*;

public class no2744 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();

        for (int i = 0; i < str.length(); i++) {
            //대문자일 경우
            char ch = str.charAt(i);
            if(Character.isUpperCase(ch)){
                ch = Character.toLowerCase(ch);
            }
            //소문자일 경우
            else {
                ch = Character.toUpperCase(ch);
            }
            bw.write(ch);
        }
        bw.flush();
        bw.close();
    }
}
