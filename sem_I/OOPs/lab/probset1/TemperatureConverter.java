/* 8. Write a class TemperatureConverter with ststic methods to convert tempertures between Celsius and Fahrenheit. */

import java.util.Scanner;

public class TemperatureConverter{
    static float celsious, fahrenheit;

    public static float temperatureConverterCtoF(float celsious){
        fahrenheit = ((celsious * 9/5) + 32);
        return fahrenheit;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the temperature(C): ");
        celsious = sc.nextInt();
        System.out.println("Temperature(F): "+ temperatureConverterCtoF(celsious));
    
    }
}