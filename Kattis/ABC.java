public class ABC
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int[] n = new int[3];
        for(int i = 0; i < 3; i++){
            n[i] = sc.nextInt();
        }
        String s = sc.next();
        int[] o = new int[3];
        int min = Math.min(n[0], Math.min(n[1], n[2]));
        int max = Math.max(n[0], Math.max(n[1], n[2]));
        int mid;
        if(n[0] != min && n[0] != max)mid = n[0];
        else if(n[1] != min && n[1] != max)mid = n[1];
        else mid = n[2];
        for(int i = 0; i < 3; i++){
            char c = s.charAt(i);
            if(c == 65)o[i] = min;
            else if(c == 66)o[i] = mid;
            else o[i] = max;
        }
        String p = "";
        for(int l: o)p += l + " ";
        System.out.println(p.trim());
    }
}
