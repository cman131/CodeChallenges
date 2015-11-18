import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Typoglycema {
	public Typoglycema() {
	}

    private static String strListToString(ArrayList<String> listy) {
        String ret = "";
        for(String o : listy) {
            ret += o.toString();
        }
        return ret;
    }

	public String getConverted(String sentence) {
		String[] wordList = sentence.split(" ");
        String result = "";
		for(String word : wordList) {
			ArrayList<String> midChars = new ArrayList<String>();
			for(int i=1; i<word.length()-1; i++) {
                midChars.add(Character.toString(word.charAt(i)));
            }
            Collections.shuffle(midChars);
            result += word.charAt(0)+Typoglycema.strListToString(midChars)+word.charAt(word.length()-1)+" ";
        }
        return result;
	}
        public static void main(String[] args) {
            Scanner scan = new Scanner(System.in);
            System.out.print("Gimme a sentence: ");
            String word = scan.nextLine();
            Typoglycema t = new Typoglycema();
            System.out.println(t.getConverted(word));
        }
}