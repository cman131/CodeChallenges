import java.io.*;
import java.util.ArrayList;

/**
 * Created by conor on 10/21/2015.
 */
public class RuthAaronPairs {
    public static ArrayList<Integer> getPrimeFactors(Integer num) {
        ArrayList<Integer> primes = new ArrayList<Integer>();
        for(int i=2; i<=num; i++) {
            if(num % i == 0) {
                primes.add(i);
                num /= i;
            }
        }
        return primes;
    }
    public static boolean isPair(String line) {
        String[] parted = line.split(",");
        int first = Integer.parseInt(parted[0].substring(1));
        int second = Integer.parseInt(parted[1].substring(0,parted[1].length()-1));

        if(first - second != 1 && first - second != -1) {
            return false;
        }

        ArrayList<Integer> firstPrimes = getPrimeFactors(first);
        ArrayList<Integer> secondPrimes = getPrimeFactors(second);
        int firstTotal = 0;
        int secondTotal = 0;
        for(int i : firstPrimes) {
            firstTotal += i;
        }
        for(int i : secondPrimes) {
            secondTotal += i;
        }
        return firstTotal==secondTotal;
    }
    public static void main(String[] args) {
        try {
            BufferedReader bufIn = new BufferedReader(new InputStreamReader(new FileInputStream("./RuthAaronTest.yoho")));
            String line;
            int duration = -1;
            while ((line = bufIn.readLine()) != null){
                if (duration<0) {
                    duration = Integer.parseInt(line);
                } else {
                    System.out.print(line+' ');
                    System.out.println(isPair(line) ? "VALID" : "NOT VALID");
                }
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
