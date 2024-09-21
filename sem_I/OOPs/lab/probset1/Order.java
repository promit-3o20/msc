/*4. Design a class Order that keeps track of total orders placed using a static variable totalOrders. Use a static block to initialize the variable and static methods to increament and display the total orders. */

import java.util.*;

public class Order{
    // golbal variables
    static int totalOrders;
    //static block
    static{
        totalOrders = 0;
    }
    //methods
    public static void ordersPlaced(){
        while (true) {
            System.out.println("Want to visit the website? [y/n] ");
            Scanner sc = new Scanner(System.in);
            String c = sc.nextLine();

            if ("n".equals(c)) {
                break;
            }
            System.out.println("Order placed successfully.");
            totalOrders++;
        }
        System.out.println("Total orders placed: " + totalOrders);
    }
    public static void main(String[] args) {
        ordersPlaced();
    }
}