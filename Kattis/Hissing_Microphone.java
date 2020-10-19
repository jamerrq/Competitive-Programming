import java.util.Scanner;
class Hissing_Microphone{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String m = s.next();
        if(m.contains("ss"))System.out.println("hiss");
        else System.out.println("no hiss");
        s.close();
    }
}
