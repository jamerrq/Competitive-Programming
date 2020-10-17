import java.util.Scanner;
import java.util.ArrayList;
public class Datum
{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int day = s.nextInt();
        int month = s.nextInt();
        String[] Jan = new String[31];
        String[] Feb = new String[28];
        String[] Mar = new String[31];
        String[] Apr = new String[30];
        String[] May = new String[31];
        String[] Jun = new String[30];
        String[] Jul = new String[31];
        String[] Aug = new String[31];
        String[] Sep = new String[30];
        String[] Oct = new String[31];
        String[] Nov = new String[30];
        String[] Dec = new String[31];
        ArrayList<String> Year = new ArrayList<>();
        for(int i = 0; i < 365; i++){
            if(i % 7 == 0)Year.add("Thursday");
            if(i % 7 == 1)Year.add("Friday");
            if(i % 7 == 2)Year.add("Saturday");
            if(i % 7 == 3)Year.add("Sunday");
            if(i % 7 == 4)Year.add("Monday");
            if(i % 7 == 5)Year.add("Tuesday");
            if(i % 7 == 6)Year.add("Wednesday");
        }
        for(int i = 0;i < Jan.length;i++){Jan[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Feb.length;i++){Feb[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Mar.length;i++){Mar[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Apr.length;i++){Apr[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < May.length;i++){May[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Jun.length;i++){Jun[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Jul.length;i++){Jul[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Aug.length;i++){Aug[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Sep.length;i++){Sep[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Oct.length;i++){Oct[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Nov.length;i++){Nov[i] = Year.get(0); Year.remove(0);}
        for(int i = 0;i < Dec.length;i++){Dec[i] = Year.get(0); Year.remove(0);}
        if(month == 1)System.out.println(Jan[day - 1]);
        if(month == 2)System.out.println(Feb[day - 1]);
        if(month == 3)System.out.println(Mar[day - 1]);
        if(month == 4)System.out.println(Apr[day - 1]);
        if(month == 5)System.out.println(May[day - 1]);
        if(month == 6)System.out.println(Jun[day - 1]);
        if(month == 7)System.out.println(Jul[day - 1]);
        if(month == 8)System.out.println(Aug[day - 1]);
        if(month == 9)System.out.println(Sep[day - 1]);
        if(month == 10)System.out.println(Oct[day - 1]);
        if(month == 11)System.out.println(Nov[day - 1]);
        if(month == 12)System.out.println(Dec[day - 1]);
        s.close();
    }
}
