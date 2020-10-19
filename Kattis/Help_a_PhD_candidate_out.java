import java.util.Scanner;
class Help_a_PhD_candidate_out{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for(int i = 0; i < n; i++){
            String p = s.next();
            if(p.charAt(0) == 'P')System.out.println("skipped");
            else{
                String a = "";
                String b = "";
                boolean plus = false;
                for(int j = 0; j < p.length(); j++){
                    if(!plus && p.charAt(j) != '+')a += p.charAt(j);
                    if(plus)b += p.charAt(j);
                    if(p.charAt(j) == '+')plus = true;
                }
                System.out.println(Integer.parseInt(b) + Integer.parseInt(a));
            }
        }
        s.close();
    }
}
