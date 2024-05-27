package stirng;

import java.util.Scanner;

public class no2744 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        // 입력 받은 문자열을 한 문자씩 처리하기 위해 문자 배열로 변환
        //char[] ch = str.toCharArray();
        for(int i = 0; i < str.length(); i++){
            // 대문자인 경우
            char ch = str.charAt(i);
            if(Character.isUpperCase(ch)){
                ch = Character.toLowerCase(ch);
            }
            // 소문자인 경우
            else{
                ch = Character.toUpperCase(ch);
            }
            System.out.print(ch);
        }
    }
}
