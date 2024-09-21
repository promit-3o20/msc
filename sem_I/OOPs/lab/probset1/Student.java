/*3.  Design a Student class where each student has a unique ID. Use a static variable to maintain a counter for the number of the students created. Create a static method to print the next available student ID.*/
import java.util.*;

public class Student {

    //global variables
    static int counter;
    static int stuId;

    // static block
    static {
        counter = 0;
        stuId = 0;
    }
    // constractors

    // methods
    public static void nextStudentId() {
        System.out.println("The next student unique ID:" + (stuId + 1));
    }

    public static void studentAdmission() {
        while (true) {
            System.out.println("Want to admit in school? [y/n] ");
            Scanner sc = new Scanner(System.in);
            String c = sc.nextLine();

            if (c.equals("n") == true) {
                break;
            }
            System.out.println("Student admitted successfully.");
            counter++;
        }
        System.out.println("Student's unique ID:" + counter);
        nextStudentId();
    }

    public static void main(String[] args) {
        studentAdmission();
    }
}
