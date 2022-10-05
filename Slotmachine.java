import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Slotmachine {
    public static int getRandomNumber(int minim, int maxim){
        int val = ThreadLocalRandom.current().nextInt(minim, maxim+1);
        return val;
    }
    public static void main(String[] args){
        double amount = 0.0;
        String[] slotRolls = {"🍉", "🍒", "🍋", "🍑", "🔔"};
        Scanner inou = new Scanner(System.in);
        while(true){
            System.out.print("Do you want to cash in(Y) or quit(Q)?: ");
            String cho = inou.next().toUpperCase();
            if (cho.equals("Y")){
                System.out.print("How much do you want to cash in?: $");
                double cash = inou.nextDouble();
                amount+=cash;
                System.out.println("Total balance: $"+amount);
                System.out.println();
                System.out.print("Spin?(Y/N): ");
                String spin = inou.next().toUpperCase();
                while (spin.equals("Y") && amount>0){
                    int x, y, z;
                    x = getRandomNumber(0, 4);
                    y = getRandomNumber(0, 4);
                    z = getRandomNumber(0, 4);
                    String st = slotRolls[x]+slotRolls[y]+slotRolls[z];
                    System.out.println(st);
                    if (x==y && y==z){
                        amount+=15.0;
                        System.out.println("+$15");
                        System.out.println();
                    } 
                    else{
                        amount-=1.0;
                        System.out.println("-$1");
                        System.out.println();
                    }
                    if (amount<=0){
                        System.out.println("You have no balance left!");
                        break;
                    }
                    System.out.print("Spin again?(Y/N): ");
                    spin = inou.next().toUpperCase();
                }
            }
            else if (cho.equals("Q")){
                System.out.println("Quitting game....");
                break;
            }
            else{
                System.out.println("Invalid input!!");
            }
        }
        inou.close();
    }
}
