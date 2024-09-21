/* 1. Implement a class called WebsiteVisitor that track the number of visitors to a website. Each time an object of WebsiteVisitor is called, increament a static counter variable and display the total number of visitors. */

import java.util.*;

public class WebsiteVisitor {

    static int counter = 0;

    // methods
    public static void website() {
        System.out.println("Website visited!");
    }

    public static void websiteTracker() {
        while (true) {
            System.out.println("Want to visit the website? [y/n] ");
            Scanner sc = new Scanner(System.in);
            String c = sc.nextLine();

            if (c.equals("n") == true) {
                break;
            }
            website();
            counter++;
        }
        System.out.println("Website visitor traker:" + counter);
    }

    public static void main(String[] args) {

        websiteTracker();
    }
}
