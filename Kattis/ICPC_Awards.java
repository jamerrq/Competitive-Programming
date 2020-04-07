import java.util.Scanner; import java.util.Map; import java.util.HashMap;
public class ICPC_Awards
{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int count = 0;
        Map<String, String> m = new HashMap<String, String>();
        for(int i = 0; i < n; i++){
            String u = s.next();
            String t = s.next();
            if(!m.containsKey(u)){System.out.println(u + " " + t); m.put(u,t); count++;}
            if(count == 12)break;
        }
    }
}
