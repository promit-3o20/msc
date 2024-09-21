/* 2. Create a class BankAccount with a static variable totalAccounts that track the number of accounts created. Use a static print method to print the total number of accounts. Also, initialize this static variable using a static block. */

import java.util.*;

public class BankAccount {

    static int totalAccounts;

    // static block 
    static {
        totalAccounts = 0;
    }

    //methods
    public static void totalAccountPrint() {
        while (true) {
            System.out.println("Want to create a bank account? [y/n] ");
            Scanner sc = new Scanner(System.in);
            String c = sc.nextLine();

            if (c.equals("n") == true) {
                break;
            }
            bankAccountMsg();
            totalAccounts++;
        }
        System.out.println("Total account traker:" + totalAccounts);
    }

    public static void bankAccountMsg() {
        System.out.println("Bank account is created successfully!");
    }

    public static void main(String[] args) {

        totalAccountPrint();
    }
}
