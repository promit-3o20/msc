/* 7. Design a class Employee that generates a unique employee ID using a static variable. Each time a new employee is created, the ID should increment.*/

import java.util.*;

public class Employee {

    //global variables
    static int counter;

    // static block
    static {
        counter = 0;
    }

    // methods
    public static void employeeHired() {
        while (true) {
            System.out.println("Hired? [y/n] ");
            Scanner sc = new Scanner(System.in);
            String c = sc.nextLine();

            if (c.equals("n") == true) {
                break;
            }
            System.out.println("Employee hired successfully.");
            counter++;
        }
        System.out.println("Employee joined: " + counter);
        for (int i = 1; i <= counter; i++) {
            System.out.println("Employee unique ID: " + i);
        }
    }

    public static void main(String[] args) {
        employeeHired();
    }
}
