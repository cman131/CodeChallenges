import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

/**
 * Created by conor on 10/21/2015.
 */
public class BowlingScoring {

    private String prev = "0";
    private String prev2 = "0";

    public BowlingScoring() {

    }

    private Integer getValue(String score) {
        int value = this.getBaseValue(score);
        if (score.equals("X")) {
            value += this.getBaseValue(this.prev)+this.getBaseValue(this.prev2);
            this.prev2 = this.prev;
            this.prev = "X";
        } else if (score.contains("/")) {
            value += this.getBaseValue(this.prev);
            this.prev = score.substring(0,1).equals("/") ? Integer.toString(10-this.getBaseValue(score.substring(1))) : score.substring(0,1);
            this.prev2 = score.substring(1).equals("/") ? Integer.toString(10-this.getBaseValue(score.substring(0,1))) : score.substring(1);
            this.prev = this.prev.equals("10") ? "X" : this.prev;
            this.prev2 = this.prev2.equals("10") ? "X" : this.prev2;
        } else {
            this.prev = score.substring(0,1);
            this.prev2 = score.substring(1);
        }
        return value;
    }
    private Integer getBaseValue(String score) {
        if(score.equals("X") || score.contains("/")) {
            return 10;
        }
        int var1 = score.substring(0,1).equals("-") ? 0 : Integer.parseInt(score.substring(0,1));
        int var2 = 0;
        if (score.length()>1) {
            var2 = score.substring(1).equals("-") ? 0 : Integer.parseInt(score.substring(1));
        }
        return var1 + var2;
    }
    public Integer getScore(String scoreSheet) {
        int total = 0;
        String[] scoreSplit = scoreSheet.split(" ");
        if(scoreSplit[9].length()>2) {
            if (scoreSplit[9].substring(0,2).contains("X")) {
                this.prev2 = scoreSplit[9].substring(2).equals("/") ? Integer.toString(10-Integer.parseInt(scoreSplit[9].substring(1, 2))) : scoreSplit[9].substring(2);
                this.prev = scoreSplit[9].substring(1,2).equals("/") ? Integer.toString(10-Integer.parseInt(scoreSplit[9].substring(2))) : scoreSplit[9].substring(1,2);
                this.prev = this.prev.equals("10") ? "X" : this.prev;
                this.prev2 = this.prev2.equals("10") ? "X" : this.prev2;
                scoreSplit = scoreSheet.substring(0, scoreSheet.length() - 2).split(" ");
            } else {
                this.prev = scoreSplit[9].substring(2);
                scoreSplit = scoreSheet.substring(0, scoreSheet.length() - 1).split(" ");
            }
        }
        for(int i = 9; i>=0; i--) {
            int val = getValue(scoreSplit[i]);
            total += val;
        }

        return total;
    }
    public static void main(String[] args) {
        try {
            BufferedReader bufIn = new BufferedReader(new InputStreamReader(new FileInputStream("./BowlingScoringTest.yoho")));
            String line;
            int duration = -1;
            BowlingScoring dat = new BowlingScoring();
            while ((line = bufIn.readLine()) != null){
                System.out.println(dat.getScore(line));
                dat = new BowlingScoring();
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
