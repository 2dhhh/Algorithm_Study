package stirng;

import java.util.Scanner;

public class no1157 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();

        int[] intArray = new int[26];
        String str2 = str1.toUpperCase();
        char[] charArray = str2.toCharArray();
        int maxIndex = 0;
        int count = 0;

        for (char c : charArray) {
            intArray[c - 'A']++;
        }

        for (int i = 1; i < intArray.length; i++) {

            if (intArray[i] > intArray[maxIndex]) {
                count = 0;
                maxIndex = i;
            }

            else if(intArray[i] == intArray[maxIndex]) {
                count++;
            }
        }
        if(count > 0){
            System.out.println("?");
        }
        else if(count == 0){
            char maxChar = (char) (maxIndex + 'A');
            System.out.println(maxChar);
        }
    }
}

