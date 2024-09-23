/* 9. Create a class OlineExam with a static methods startTimer that starts a countdown timer for an Online exam. Use a static block to initialize default timer setting( e.g., exam duration, interval between updates.)*/

public class OnlineExam {

    static int totalTime, interval;

    static {
        totalTime = 120;
        interval = 30;
    }

    public static void startTimer() {
        int remainingTime = totalTime;

        System.out.println("Exam start.");
        while (remainingTime >= 0) {
            System.out.println("Remaining time " + (remainingTime / 60) + " minutes " + (remainingTime % 60) + " seconds");
            try {
                Thread.sleep(interval * 1000);  // Wait for the interval (convert seconds to milliseconds)
            } catch (InterruptedException e) {
                System.out.println("Timer interrupted.");
            }
            remainingTime -= interval;
        }
        System.out.println("Exam end.");
    }

    public static void main(String[] args) {
        startTimer();
    }
}
