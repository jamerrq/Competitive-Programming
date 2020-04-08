public class Paradox_With_Averages
{
    static boolean joke(double ncs, double ne, double ccs, double ce, double s){
        return (ccs - s) / (ncs - 1) > ccs / ncs && (ce + s) / (ne + 1) > ce / ne;
    }
    
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int cases = sc.nextInt();
        for(int i = 0; i < cases; i++){
            sc.nextLine();
            int ncs = sc.nextInt(), ne = sc.nextInt();
            int[] cs = new int[ncs], e = new int[ne];
            int ccs = 0, ce = 0;
            for(int j = 0; j < ncs; j++){
                int s = sc.nextInt();
                cs[j] = s;
                ccs += s;
            }
            for(int j = 0; j < ne; j++){
                int s = sc.nextInt();
                e[j] = s;
                ce += s;
            }
            int count = 0;
            for(int j = 0; j < ncs; j++){
                if(joke(ncs, ne, ccs, ce, cs[j]))count++;
            }
            System.out.println(count);
        }
    }
}
