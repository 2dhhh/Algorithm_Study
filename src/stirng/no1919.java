package stirng;

import java.util.Scanner;

public class no1919 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();

        // 지워야할 문자개수 카운팅
        int sum = 0;

        // 알파벳 개수를 저장할 정수 배열 선언
        int[] intArray = new int[26];

        // str1 알파벳 배열에 저장
        for(int i = 0; i < str1.length(); i++){
            intArray[str1.charAt(i) - 'a']++;
        }

        // str2 알파벳 배열에 저장
        for(int i = 0; i < str2.length(); i++){
            intArray[str2.charAt(i) - 'a']--;
        }

        // 문자 개수 비교
        for(int i = 0; i < 26 ; i++){
            sum += Math.abs(intArray[i]);
        }
        System.out.println(sum);
    }
}
