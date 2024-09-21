/* 6. Create a Product with static variable to store VAT and discount rates applicable to all products. Implement static method to calculate the final price of a product based on this base price and the static rates. */

import java.util.Scanner;

public class Product{
    //global variabls
    static float  vat, discount;
    //methods
    public static float calculateFinalPrice(float basePrice,float  vat, float discount) {
        float priceAfterDiscount = basePrice - (basePrice * discount/100);  // Apply discount
        float finalPrice = priceAfterDiscount + (priceAfterDiscount * vat/100);  // Apply VAT
        return finalPrice;
    }
    public static void main(String[] args) {
        System.out.println("Enter the product base Price: ");
        Scanner sc = new Scanner(System.in);
        float base = sc.nextFloat();
        System.out.println("Enter the product VAT: ");
        Scanner v = new Scanner(System.in);
        vat = v.nextFloat();
        System.out.println("Enter the product discount rate: ");
        Scanner d = new Scanner(System.in);
        discount = d.nextFloat();
        
        System.out.println("Final price: "+ calculateFinalPrice(base,vat,discount));
    }
}