/* 5. Create a class Course that has a static variable totalCourses. Each time a course is created, the static variable should be increamented. Create a static method that prints the total number of courses offered by the university. */

import java.util.Scanner;

public class Course {

    //global variabls
    static int totalCourses;

    //static block
    static {
        totalCourses = 0;
    }

    //methods
    public static void createCourse() {
        while (true) {
            System.out.println("Create course? [y/n] ");
            Scanner sc = new Scanner(System.in);
            String c = sc.nextLine();

            if (c.equals("n") == true) {
                break;
            }
            System.out.println("Course created.");
            totalCourses++;
        }
        System.out.println("Total Courses:" + totalCourses);
    }
    public static void main(String[] args) {
        Course.createCourse();
    }
}
