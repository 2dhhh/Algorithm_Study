package stirng;

import java.util.Scanner;

public class no13223 {
    public static void main(String[] args) {

        // 입력
        Scanner sc = new Scanner(System.in);
        String[] currentTime = sc.nextLine().split(":");
        String[] dropTime = sc.nextLine().split(":");

        int currentH = Integer.parseInt(currentTime[0]);
        int currentM = Integer.parseInt(currentTime[1]);
        int currentS = Integer.parseInt(currentTime[2]);
        int currentTotalSecond = currentH * 3600 + currentM * 60 + currentS;

        int dropH = Integer.parseInt(dropTime[0]);
        int dropM = Integer.parseInt(dropTime[1]);
        int dropS = Integer.parseInt(dropTime[2]);
        int dropTotalSecond = dropH * 3600 + dropM * 60 + dropS;

        int differenceSecond = dropTotalSecond - currentTotalSecond;

        if(differenceSecond <= 0){
            differenceSecond += (24*3600);
        }
        int h = differenceSecond / 3600;
        int m = (differenceSecond % 3600) / 60;
        int s = differenceSecond % 60;

        System.out.printf("%02d:%02d:%02d",h,m,s);



    }

}
